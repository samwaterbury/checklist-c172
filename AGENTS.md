# Repository guidance

This project renders a personal C172S G1000 checklist from YAML using Typst. The current output is four 5.5 × 8.5 in pages: two duplex kneeboard cards. The normal card covers preflight through shutdown; the emergency card groups engine failures and forced landings on one side and fires on the other. All 27 authored procedures appear once.

Use the [README](README.md) for everyday build, watch, and test commands.

## Toolchain and printing

Rendering requires **Typst 0.15.1** and Helvetica Neue (Medium, Light, Light Italic, Bold, Bold Italic) plus Helvetica Bold. The PDF embeds font subsets; this repository does not redistribute fonts. No Python, Node, web server, or external Typst packages are needed to render.

`scripts/typst` checks the compiler version and prefers `TYPST`, then the local compiler under `.tools/`, then PATH. To install on an Apple Silicon Mac:

```sh
mkdir -p .tools
curl -fL https://github.com/typst/typst/releases/download/v0.15.1/typst-aarch64-apple-darwin.tar.xz \
  -o .tools/typst.tar.xz
tar -xJf .tools/typst.tar.xz -C .tools
make build
```

On another platform, install the matching [official release](https://github.com/typst/typst/releases/tag/v0.15.1) and put it on PATH or set `TYPST=/absolute/path/to/typst`. Replacing fonts requires a visual layout check.

Print at **100% / actual size**. Pair pages 1–2 and 3–4 for duplex printing; check orientation with a proof sheet before laminating. Larger stock can be trimmed without scaling. Footers contain only the section and aircraft names.

## Content and layout

| File | Purpose |
|---|---|
| [content/procedures.yaml](content/procedures.yaml) | Procedure text, qualifiers, notes, and nested groups |
| [layout/kneeboard.yaml](layout/kneeboard.yaml) | Paper dimensions, margins, card pairing, and explicit column placement |
| [theme.typ](theme.typ) | Typography, colors, and spacing |
| [components.typ](components.typ) | Rows, notes, groups, sections, validation, and overflow checks |
| [sheet.typ](sheet.typ) | Column geometry |
| [main.typ](main.typ) | Document setup, footers, and page rendering |

```yaml
- id: se-bus-e
  type: check
  challenge: "BUS E Volts"
  qualifier: "Min 24 volts"
  response: "Check"
```

A `check` generates parentheses around its optional qualifier and period leaders between challenge and response. Add `notes: ["Supporting text"]` below a row. A standalone `note` has a `text` field. A `branch` has a `condition` and child `blocks`; a `subprocedure` has a `title` and child `blocks`. Groups are boxed by default. `boxed: false` displays a centered bold italic heading. Groups may nest.

Keep IDs stable when moving or editing items. Quote text values, particularly `"ON"`, `"OFF"`, and frequencies. Use `\n` inside double-quoted strings for intentional line breaks. Spelling and capitalization are preserved. Keep YAML files free of comments; put maintenance explanations here or in `docs/`.

The theme uses 8 pt actions, 9 pt section headings, 7 pt notes and conditional headings, 6 pt qualifiers, and 10 pt footers. Top and side margins are 18 pt; the footer region is 36 pt, with a separate 12 pt buffer above it. Paper size remains configurable; changing it may require rearranging procedures.

Columns at least 90% full can stretch vertical spacing up to twice its natural value. Sparse columns retain natural spacing. Boxes and conditional headings have extra surrounding space; conditional capitals also receive a small optical alignment adjustment. Fonts never shrink to fit. Long responses wrap below their challenge, and headers grow when necessary. Overfull columns and unbreakable words abort the build with a diagnostic instead of moving or dropping content.

After a failed build, Typst may leave the **last successful PDF** in place. Check build output before using it.

## Verification

The tests check the four-page layout, card pairing, fonts and sizes, every procedure's text and order, margins and footer clearance, spacing, wrapping, and validation failures. Synthetic examples live in `tests/fixture.typ`.

The independent reference check reads [original.pdf](original.pdf), normalizes typographic differences, and applies only the reviewed exceptions in [tests/fixtures/reference-changes.json](tests/fixtures/reference-changes.json). That fixture includes separately transcribed expectations for the two added fire procedures. It is not generated from the content being tested. Update relevant expectations only after reviewing an intentional wording change. See [fixture guidance](tests/fixtures/README.md).

Render changed pages to images and inspect them after layout changes. These checks establish document reproduction, not operational correctness.

## Decisions and research

[Content decisions](docs/content-decisions.md) is the authoritative record of implemented changes, retained differences, and outstanding review. The original audits remain historical evidence:

- [POH notes and conditions audit](docs/poh-note-condition-review.md)
- [Emergency coverage and wording audit](docs/emergency-procedure-review.md)
- [Rendering approaches and conventions](docs/research.md)
- [Physical-format references](docs/checklist-format-reference.md)
- [Text-size experiments](docs/text-size-study.md)

The comparison layouts and their supporting code were retired after selecting this format. Commit `9174e4a` preserves their last implementation. `tmp/` is ignored scratch space; the useful local POH extraction remains under `tmp/poh-review/`. The current PDF and original reference PDF remain tracked in Git.
