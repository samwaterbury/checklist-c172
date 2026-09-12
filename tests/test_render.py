"""Exercise rendered content and layout failure modes, not PDF byte equality."""
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

import pdfplumber
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
COMPILER = ROOT / "scripts" / "typst"


def normalize(text):
    return re.sub(r"\s+", " ", re.sub(r"\.{2,}", " ", text)).strip()


def compile_pdf(target, output, *args):
    return subprocess.run(
        [str(COMPILER), "compile", "--root", str(ROOT), *args, str(target), str(output)],
        cwd=ROOT, capture_output=True, text=True,
    )


class RenderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = tempfile.TemporaryDirectory(prefix="checklist-tests-")
        cls.addClassCleanup(cls.directory.cleanup)
        cls.pdf = Path(cls.directory.name) / 'checklist.pdf'
        result = compile_pdf(ROOT / 'main.typ', cls.pdf)
        if result.returncode or result.stderr.strip():
            raise AssertionError(result.stderr)
        query = subprocess.run(
            [str(COMPILER), "eval", "--root", str(ROOT), "--in", "tests/data.typ",
             'query(<source-data>).first().value', "--format", "json"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        cls.data = json.loads(query.stdout)

    def fixture(self, mode, expected_error=None):
        output = Path(self.directory.name) / f"{mode}.pdf"
        result = compile_pdf(ROOT / "tests/fixture.typ", output, "--input", f"case={mode}")
        if expected_error:
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(expected_error, result.stderr)
            self.assertFalse(output.exists(), "Failed builds must not emit a new PDF")
        else:
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(result.stderr.strip(), result.stderr)
        return output

    def test_pages_fonts_and_type_sizes(self):
        reader = PdfReader(self.pdf)
        self.assertEqual(len(reader.pages), 4)
        width, height = 396, 612
        names = []
        for page in reader.pages:
            self.assertEqual(tuple(float(v) for v in page.mediabox), (0, 0, width, height))
            for font_ref in page['/Resources']['/Font'].values():
                font = font_ref.get_object()
                if '/DescendantFonts' in font:
                    font = font['/DescendantFonts'][0].get_object()
                names.append(str(font['/BaseFont']))
                descriptor = font['/FontDescriptor'].get_object()
                self.assertTrue(any(k in descriptor for k in ('/FontFile', '/FontFile2', '/FontFile3')))
        self.assertTrue(any('HelveticaNeue-Medium' in n for n in names))
        self.assertTrue(any('HelveticaNeue-LightItalic' in n for n in names))
        with pdfplumber.open(self.pdf) as document:
            sizes = {round(c['size'], 2) for page in document.pages for c in page.chars}
            expected_sizes = {6, 7, 8, 9, 10}
            self.assertEqual(sizes, expected_sizes)

    def test_all_placed_content_survives_in_order(self):
        def expected(blocks):
            for item in blocks:
                if item['type'] == 'check':
                    yield item['challenge']
                    if 'qualifier' in item:
                        yield '(' + item['qualifier'] + ')'
                    yield item['response']
                    yield from item.get('notes', [])
                elif item['type'] in ('branch', 'subprocedure'):
                    yield item.get('condition', item.get('title'))
                    yield from expected(item['blocks'])
                else:
                    yield item['text']

        procedures = self.data['procedures']
        placed = []
        reader = PdfReader(self.pdf)
        for page, plan in zip(reader.pages, self.data['plan']['pages'], strict=True):
            text = normalize(page.extract_text())
            self.assertNotIn('AIRPORT INFORMATION', text)
            cursor = 0
            for column in plan['columns']:
                for pid in column:
                    placed.append(pid)
                    procedure = procedures[pid]
                    for phrase in [procedure['title'], *expected(procedure['blocks'])]:
                        phrase = normalize(phrase)
                        index = text.find(phrase, cursor)
                        self.assertGreaterEqual(index, cursor, f'missing/out-of-order in {pid}: {phrase}')
                        cursor = index + len(phrase)
        self.assertCountEqual(placed, procedures)

    def test_printed_content_stays_inside_sheet(self):
        with pdfplumber.open(self.pdf) as document:
            for page in document.pages:
                for char in page.chars:
                    if char['text'].isspace():
                        continue
                    self.assertGreaterEqual(char['x0'], 8)
                    self.assertLessEqual(char['x1'], page.width - 8)
                    self.assertGreaterEqual(char['top'], 8)
                    self.assertLessEqual(char['bottom'], page.height - 4)

    def test_transcription_matches_reference_after_rearrangement(self):
        # Read independently from original.pdf, then compare each intact procedure.
        # Source coordinates are fixed; output coordinates follow its chosen layout.
        def reference_text(page, bounds):
            # Generated leaders can contain just one dot at narrow widths.
            # Remove their Light-face glyphs, preserving decimal points in body text.
            region = page.crop(bounds).filter(lambda obj: not (
                obj.get('object_type') == 'char' and obj.get('text') == '.'
                and obj.get('fontname', '').endswith('HelveticaNeue-Light')))
            text = region.extract_text(x_tolerance=1, y_tolerance=3)
            text = text.translate(str.maketrans({'—': '-', '–': '-', '“': '"', '”': '"', '…': '.'}))
            text = re.sub(r'\.{2,}', '', text).replace('Fuel Filler Cap .', 'Fuel Filler Cap ')
            return re.sub(r'\s+', '', text)

        titles = {pid: procedure['title'] for pid, procedure in self.data['procedures'].items()}
        titles['engine-out-flight-brief'] = titles['engine-out-flight']

        def split_procedures(text, ids):
            parts = {}
            cursor = 0
            for i, pid in enumerate(ids):
                title = re.sub(r'\s+', '', titles[pid])
                self.assertTrue(text.startswith(title, cursor), f'Cannot locate header for {pid}')
                if i + 1 < len(ids):
                    next_title = re.sub(r'\s+', '', titles[ids[i + 1]])
                    end = text.find(next_title, cursor + len(title))
                    self.assertGreater(end, cursor)
                else:
                    end = len(text)
                parts[pid] = text[cursor:end]
                cursor = end
            return parts

        original_columns = ((9, 198.5), (198.6, 387.2), (406, 595), (595.1, 785))
        reference_order = [
            [['engine-out-takeoff', 'engine-out-after-takeoff', 'engine-out-flight-brief'], ['ditching'],
             ['engine-out-flight', 'landing-with-power', 'landing-no-power', 'engine-fire-flight'],
             ['engine-fire-start', 'electrical-fire']],
            [['after-start', 'run-up', 'before-takeoff'],
             ['after-takeoff', 'cruise', 'approach', 'before-landing', 'after-landing', 'shutdown'],
             ['preflight-cabin', 'preflight-empennage', 'preflight-right-wing', 'preflight-nose'],
             ['preflight-left-wing', 'before-starting-engine', 'starting-engine']],
        ]
        source = {}
        with pdfplumber.open(ROOT / 'original.pdf') as original:
            for p in range(2):
                for c, (x0, x1) in enumerate(original_columns):
                    bottom = 344 if p == 0 and c < 2 else 603
                    text = reference_text(original.pages[p], (x0, 9, x1, bottom))
                    if p == 0 and c == 1:
                        text, marker, _ = text.partition('AFTERLANDING')
                        self.assertTrue(marker)
                    source.update(split_procedures(text, reference_order[p][c]))
        changes = json.loads((ROOT / 'tests/fixtures/reference-changes.json').read_text())
        def compact(lines):
            return re.sub(r'\s+', '', ' '.join(lines))

        for change in changes['replacements']:
            pid = change['procedure']
            before, after = compact(change['before']), compact(change['after'])
            self.assertEqual(source[pid].count(before), 1, pid)
            source[pid] = source[pid].replace(before, after)
        for pid, ending in changes['endings'].items():
            self.assertTrue(source[pid].endswith(compact(ending['after'])), pid)
            source[pid] += compact(ending['append'])
        source.update({pid: compact(lines) for pid, lines in changes['additions'].items()})
        plan = self.data['plan']
        with pdfplumber.open(self.pdf) as document:
            for page, placement in zip(document.pages, plan['pages'], strict=True):
                columns = placement['columns']
                gutter = plan['column_gutter_pt']
                width = (plan['width_pt'] - 2 * plan['margin_pt'] - (len(columns) - 1) * gutter) / len(columns)
                for i, ids in enumerate(columns):
                    x0 = plan['margin_pt'] + i * (width + gutter)
                    bounds = (x0, plan.get('top_margin_pt', plan['margin_pt']), x0 + width,
                              plan['height_pt'] - plan['bottom_margin_pt'])
                    text = reference_text(page, bounds)
                    for pid, actual in split_procedures(text, ids).items():
                        with self.subTest(procedure=pid):
                            self.assertEqual(source[pid], actual)

    def test_poh_response_alternatives_use_action_type(self):
        with pdfplumber.open(self.pdf) as document:
            for left, right in ((18, 192), (204, 378)):
                page = document.pages[2]
                # Ditching has its own POH note with the same numbers; P1 covers
                # only the earlier flap-dependent action responses.
                bottom = page.search('LANDING - WITH POWER')[0]['top'] if left == 204 else 564
                column = page.crop((left, 18, right, bottom))
                words = column.extract_words(extra_attrs=['size', 'fontname'])
                speeds = [w for w in words if w['text'] in ('70', '65')]
                self.assertEqual([w['text'] for w in speeds], ['70', '65'])
                self.assertLess(speeds[0]['top'], speeds[1]['top'])
                for word in speeds:
                    self.assertAlmostEqual(word['size'], 8)
                    self.assertIn('HelveticaNeue-Medium', word['fontname'])

    def test_nearly_full_columns_align_without_stretching_sparse_pages(self):
        with pdfplumber.open(self.pdf) as document:
            for index, page in enumerate(document.pages):
                bottoms = []
                for left, right in ((18, 192), (204, 378)):
                    chars = [c for c in page.chars if left <= c['x0'] < right
                             and c['top'] < 576 and not c['text'].isspace()]
                    # Baselines avoid font-specific descender bounds.
                    bottoms.append(max(page.height - c['matrix'][5] for c in chars))
                for column, bottom in enumerate(bottoms):
                    if index < 2:
                        self.assertAlmostEqual(bottom, 564, delta=0.05)
                    else:
                        self.assertLess(bottom, 18 + 0.9 * 546)
                body = [c for c in page.chars if c['top'] < 576 and not c['text'].isspace()]
                footer = [c for c in page.chars if c['top'] >= 576 and not c['text'].isspace()]
                self.assertGreaterEqual(min(c['top'] for c in footer)
                                        - max(c['bottom'] for c in body), 12)

    def test_current_emergency_grouping_and_cabin_condition(self):
        with pdfplumber.open(self.pdf) as document:
            groups = (
                (2, (204, 18, 378, 576), ('LANDING - NO POWER', 'LANDING - WITH POWER', 'LANDING - DITCHING')),
                (3, (18, 18, 192, 576), ('ENGINE FIRE DURING START', 'ENGINE FIRE IN FLIGHT')),
                (3, (204, 18, 378, 576), ('ELECTRICAL FIRE IN FLIGHT', 'CABIN FIRE', 'WING FIRE')),
            )
            for index, bounds, headings in groups:
                text = normalize(document.pages[index].crop(bounds).extract_text())
                positions = [text.index(heading) for heading in headings]
                self.assertEqual(positions, sorted(positions))
            page = document.pages[3]
            cabin_top = page.search('CABIN FIRE')[0]['bottom']
            wing_top = page.search('WING FIRE')[0]['top']
            cabin = page.crop((204, cabin_top, 378, wing_top))
            condition = cabin.search('IF FIRE HAS BEEN EXTINGUISHED')[0]
            opened = cabin.search('Cabin Vents.*OPEN')[0]
            self.assertLess(condition['top'], opened['top'])
            self.assertTrue(all('BoldItalic' in c['fontname'] for c in condition['chars']))

    def test_kneeboard_cards_pair_and_respect_margins(self):
        cards = ('N1', 'E1')
        plan = self.data['plan']
        with pdfplumber.open(self.pdf) as document:
            for card_index, card in enumerate(cards):
                for offset, side in enumerate(('A', 'B')):
                    index = card_index * 2 + offset
                    page = document.pages[index]
                    placement = plan['pages'][index]
                    self.assertEqual((placement['card'], placement['side']), (card, side))
                    footer = page.crop((0, page.height - plan['bottom_margin_pt'], page.width, page.height))
                    self.assertEqual(normalize(footer.extract_text()), f'{placement["name"]} C172S G1000')
                    for char in page.chars:
                        if not char['text'].isspace():
                            self.assertGreaterEqual(char['top'], plan['top_margin_pt'])
                            self.assertGreaterEqual(char['x0'], 18)
                            self.assertLessEqual(char['x1'], 378)
                    for rect in page.rects:
                        self.assertGreaterEqual(rect['top'], plan['top_margin_pt'] - 0.5)
                    categories = {self.data['procedures'][pid]['category']
                                  for col in placement['columns'] for pid in col}
                    self.assertEqual(categories, {'emergency' if card.startswith('E') else 'normal'})

    def test_invalid_category_is_rejected(self):
        self.fixture('category', 'Unknown section category')

    def test_long_response_wraps_without_shrinking(self):
        output = self.fixture('wrap')
        text = normalize(PdfReader(output).pages[0].extract_text())
        self.assertIn('KEEP EVERY WORD IN THIS LONG EXAMPLE RESPONSE', text)
        self.assertIn('(only under this example condition)', text)
        self.assertIn('A supporting note remains attached below its response.', text)
        with pdfplumber.open(output) as pdf:
            words = pdf.pages[0].extract_words(x_tolerance=1)
            challenge = next(w for w in words if w['text'] == 'Example')
            response = next(w for w in words if w['text'] == 'KEEP')
            self.assertGreater(response['top'], challenge['bottom'])
            for char in pdf.pages[0].chars:
                # PDF extraction retains trailing spaces beyond the line's ink bounds.
                if char['text'].isspace():
                    continue
                self.assertGreaterEqual(char['x0'], 11.9)
                # Optical punctuation overhang is smaller than 1pt; letters must fit.
                allowance = 1 if char['text'] in '.,;:!?' else 0.1
                self.assertLessEqual(char['x1'], 162 + allowance)
            sizes = {round(c['size'], 2) for c in pdf.pages[0].chars}
            self.assertEqual(sizes, {6, 7, 8})

    def test_column_overflow_is_actionable(self):
        self.fixture('overflow', 'Layout overflow in deliberately overfull column')

    def test_unbreakable_word_is_rejected(self):
        self.fixture('word', 'Unbreakable word exceeds row width')

    def test_long_title_is_rejected(self):
        self.fixture('title', 'Unbreakable word in section title')

    def test_duplicate_ids_are_rejected(self):
        self.fixture('duplicate', 'Duplicate block id')

    def test_missing_procedure_is_rejected(self):
        self.fixture('missing', 'Unknown procedure')

    def test_nested_groups_keep_all_text(self):
        output = self.fixture('nested')
        text = normalize(PdfReader(output).pages[0].extract_text())
        self.assertIn('OUTER CONDITION', text)
        self.assertIn('INNER GROUP', text)
        self.assertIn('KEEP EVERY WORD IN THIS LONG EXAMPLE RESPONSE', text)

    def test_note_word_overflow_is_rejected(self):
        self.fixture('note-word', 'Unbreakable word in note')

    def test_long_header_wraps_without_shrinking(self):
        output = self.fixture('title-wrap')
        self.assertIn('ENGINE OUT - AFTER TAKEOFF', normalize(PdfReader(output).pages[0].extract_text()))
        with pdfplumber.open(output) as pdf:
            chars = pdf.pages[0].chars
            self.assertEqual({round(c['size'], 2) for c in chars}, {9})
            self.assertGreater(len({round(c['top'], 1) for c in chars}), 1)


if __name__ == '__main__':
    unittest.main()
