# A maintainable flight-checklist publishing system

> Historical research and experiments. Implementation claims, commands, file paths, and page counts describe the experiment at the time. The comparison layouts were retired during repository cleanup; commit `9174e4a` preserves their last implementation. See the [README](../README.md) for the maintained document.

The best starting point for this project is **structured checklist content rendered through a small Typst component library**. HTML/CSS printed with a pinned Chromium version is the strongest alternative, especially if an interactive editor becomes important. Both approaches can plausibly reproduce the supplied layout closely; neither requires building a general-purpose document engine.

The central architectural choice is to separate **procedure content, visual components, and page placement**. A reusable row should know how to place a control name, leader, qualifier, and response. A procedure should know its ordered steps and conditions. A layout file should decide which column contains that procedure. Editing any one of these should not require editing the others.

This recommendation is an engineering assessment grounded in the supplied PDF and the primary documentation cited below. It is not a comparative rendering benchmark: no replacement checklist or working renderer has been built. The exact applicable POH revision, supplements, and school checklist were not supplied, so procedure correctness and airport data currency have not been audited.

## 1. The reference document

Both pages of `original.pdf` were inspected visually and through PDF text, font, and geometry extraction. These measurements describe the exported artifact, including small inconsistencies introduced during authoring.[^1]

| Property | Observed in the PDF | Implication |
|---|---|---|
| Physical sheet | Two pages, each 792 × 612 PDF points | US Letter, **landscape**, 11 × 8.5 inches |
| Overall structure | Two side-by-side panels, each with two narrow columns | Preserve explicit panels and columns |
| Typical column width | Approximately 188.6 pt, or 2.62 inches | Long paired rows need a deliberate wrapping rule |
| Central panel gap | Approximately 19.3–19.5 pt | Treat the center as a separate gutter |
| Outer boundaries | Roughly 9–10 pt from the sheet edges | Printing margins need physical verification |
| Section bars | Usually 14.4 pt high | Good candidate for one reusable component |
| Header text | Predominantly Helvetica Bold, 9 pt, uppercase | Separate header face, size, and tracking from body styles |
| Main row typography | Predominantly Helvetica Neue Medium, 8 pt; many leader glyphs use Light | Visually strong text is usually **medium**, not bold |
| Notes | Predominantly Helvetica Neue Light Italic, 7 pt | Define one note style, with explicit exceptions |
| Inline qualifiers | Commonly 6 pt | Small qualifying text is a distinct role |
| Special emphasis | Some bold and bold italic text | Preserve meaningful emphasis separately from ordinary row weight |
| Reference table | Six columns, eight airport rows, alternating fills, spanning title/footer | A genuine table, separate from procedural lists |

At the center, the PDF has a dividing rule near x = 396 pt. Each half would be 5.5 × 8.5 inches if folded at the center. Folding or cutting is a plausible explanation of the arrangement, but is not established by the PDF alone. The initial renderer should preserve the physical placement without assuming a booklet reading order.

The page map is more intentional than a generic four-column article:

| Side | Left panel | Right panel |
|---|---|---|
| Page 1 | Engine-out procedures and ditching; after landing/shutdown; airport table across both columns below | Further engine-out/landing procedures, engine fires, electrical fire |
| Page 2 | After start through shutdown | Preflight through engine starting |

An automatically balanced multicolumn flow would not capture this structure. In particular, the airport table occupies a reserved lower region spanning the left panel, while the right panel continues independently.

### Differences worth recording before migration

Several apparent duplicates are not identical. The two **ENGINE OUT — DURING FLIGHT** sections on page 1 have different endings: the right-hand version includes an additional fuel-pump step and explanatory note. **SHUTDOWN** appears on both pages, with an additional fuel-selector item in the page-2 version. These are observations about the supplied document, not judgments about which version is correct.

**AFTER LANDING** and **SHUTDOWN** use red section bars on page 1 and gray bars on page 2. That suggests the current color sometimes identifies the side rather than the procedure category. A component system should make those separate choices: `category: normal` can coexist with a layout-specific header treatment if that is intentional.

The PDF also contains slightly different red fill values, small alignment offsets, mixed casing such as `Rich`/`RICH` and `Idle Cutoff`/`IDLE CUTOFF`, and different-looking leaders in the boxed procedures. A close recreation should normalize accidental graphical differences. Textual differences should remain visible for review rather than being silently rewritten.

## 2. Conventions, evidence, and applicability

There is useful guidance on checklist design, but the sources reviewed do not establish one universal visual specification for a personal C172 checklist. It helps to distinguish aircraft-specific procedure content, human-factors guidance, and house typography. Consistency within the finished document can be encoded precisely even when a convention is not a mandatory standard.

Three sources are particularly useful:

* **NASA CR-177549, _Human Factors of Flight-Deck Checklists: The Normal Checklist_ (1990).** This examines checklist use as well as document design. It distinguishes performing actions as they are read from checking a configuration already established. Its airline context should be considered when applying the conclusions to a single-pilot aircraft.[^2]
* **NASA CR-177605, _On the Typography of Flight-Deck Documentation_ (1992).** This reviews typography, including character height, spacing, contrast, and the reading environment. It explicitly acknowledges limited cockpit experimentation and treats its recommendations as a baseline for contextual evaluation.[^3]
* **UK CAA CAP 676, Issue 3 (2006).** Its practical guidance includes paired action/response text, linking dots or dashes, distinct notes, and clear decisions. It favors sans-serif text and mixed case for prose; italics are acceptable for notes, not drill actions. It recommends black text on a light background, with red emergency cues rather than prescribing white-on-red titles. Its suggested body size is 12 pt, minimum 10 pt; headings 14 pt, minimum 12 pt, assessed at about 600 mm. This is guidance, not a U.S. personal-checklist font regulation.[^4]

FAA AC 120-71B is also relevant to how procedures are developed and maintained. The FAA lists it as active, issued January 10, 2017, and says that although directed toward Part 121/135 air carriers, other operators, pilot schools, and training centers are encouraged to use it. It is not a stylesheet for this project.[^5]

### What to encode

The following are proposed design rules for this checklist, informed by the guidance but tailored to the supplied layout:

| Element | Recommended representation | Rendering rule |
|---|---|---|
| Phase or procedure title | `section` with title, category, stable ID | Consistent bar height, padding, type, and separation |
| Paired item | `check` with challenge and response | Left and right alignment; generated leader between them |
| Literal cockpit label | Inline `panel-label` token | Preserve its exact spelling and case |
| Ordinary equipment wording | Plain text token | Preserve authored wording; no automatic uppercasing |
| Short response qualifier | Separate `qualifier` field | Keep associated with the response; parentheses generated consistently |
| Explanation | `note` attached to a step or group | Distinct style; stay with the material it explains |
| Prerequisite or caution | Explicit role and attachment | Place before the affected action when that is its meaning |
| Conditional procedure | `branch` containing condition and child steps | Condition and its scope remain visually connected |
| Reusable subprocedure | Named group | Consistent box treatment; body consists of ordinary components |
| Cross-reference | `reference` to a procedure ID | Resolve target title and detect broken references |
| Airport information | Separate table dataset | Explicit columns, units, multiline cells, and source dates |

“IF FIRE HAS BEEN EXTINGUISHED” is a condition, not simply italic text. “If Engine Starts” and “If Engine Fails to Start” express alternative branches. “Priming Procedure” is a named subprocedure. They may share border and heading primitives without becoming the same semantic object.

Avoid inferring semantics from typography. A boxed group must not automatically mean “memory items,” and an uppercase phrase must not automatically mean “warning.” Store a memory-item designation only if established by the relevant source and intended use. Similarly, a pair of aligned phrases does not itself establish whether the list is read-do or a configuration check.

### The significant conflict: density and legibility

The reference's 8 pt body and 9 pt headings are smaller than the CAP 676 recommendations above. That is a concrete conflict between close visual fidelity and this particular human-factors baseline.[^4] A larger font is not a cosmetic adjustment: changing 8 pt to 10 pt increases nominal type size by 25%, and may also produce extra line wraps.

NASA's typography report separately discusses physical **x-height**, including a 0.10-inch recommendation, and warns that character height differs from nominal type size. Do not translate that directly into “7.2 pt text is sufficient”: the em size used by PDF typography is not the visible height of a lowercase letter.[^3]

I recommend preserving the current geometry as a reference profile and evaluating a second profile with larger type. The latter may require moving the airport table, redistributing sections, or using additional panels. It should not obtain space by silently shortening procedures or scaling everything down again.

Printed evaluation should use actual size, realistic viewing distance, the intended paper or laminate, and ordinary cockpit lighting conditions on the ground. Screen zoom obscures the tradeoff. A house style can retain the reference's familiar appearance while making an explicit, informed choice about density.

## 3. The available implementation approaches

The ratings below are judgments for this particular two-sided, tightly arranged checklist. They are not measured performance scores.

| Approach | Fit to this layout | Maintenance character | Principal tradeoff | Position |
|---|---|---|---|---|
| **Typst components + structured data** | Excellent candidate | Small document-focused codebase | New language; custom fit validation | First choice |
| **HTML/CSS + Chromium via Playwright** | Excellent candidate | Familiar browser tools; easy future UI | Browser dependency and print-specific checks | Strong alternative |
| **Python + ReportLab** | Excellent geometric control | Explicit, inspectable rendering code | More manual layout work | Strong Python option |
| **HTML/CSS + WeasyPrint** | Good candidate | Python orchestration and print CSS | Its CSS behavior differs from Chromium | Secondary HTML option |
| **LuaLaTeX/XeLaTeX** | Excellent candidate | Mature typesetting ecosystem | Macro/package complexity for a new maintainer | Best with existing TeX familiarity |
| **React PDF renderer** | Good candidate | Reusable React components | Own primitives and supported style subset | Best with a React-specific preference |
| **pdfmake** | Good for structured lists/tables | JavaScript document objects | Fine row typography needs proving | Credible secondary option |
| **QuestPDF** | Good candidate | C# composition API | .NET and eligibility-based licensing | Best in an existing .NET environment |
| **Paged.js / Vivliostyle** | Capable | Web publication tooling | Extra pagination machinery | More compelling for longer documents |
| **Prince** | Capable | Dedicated HTML-to-PDF product | Proprietary licensing | Commercial alternative |
| **Desktop publishing / Pages** | Already demonstrably capable visually | Visual editing, styles, templates | Semantic reuse needs added automation | Valid if visual editing dominates |
| **Aviation checklist editors** | Depends on export controls | Domain-specific authoring | Layout and intended-use constraints | Investigate selectively |

### Typst

Typst is a programmable typesetting system. Its compiler is free and Apache-2.0 licensed, can run locally, and supports a watch workflow; the commercial web editor is optional. There is no need to write Rust merely because the compiler is implemented in Rust.[^6]

For this design, its most relevant primitives are grids for the panels, blocks for sections, tables for airport data, a `repeat` element for leaders, and content measurement. It can read YAML directly, so a separate data-conversion program is optional.[^7][^8][^9]

The component interface could look like this, schematically:

```text
section(title, category, children)
check(challenge, response, qualifier?)
note(text, role)
branch(condition, children)
subprocedure(title, children)
airport_table(rows)
sheet(left_panel, right_panel, theme)
```

These functions would return typeset content. A change to the `check` function would update every row; a change to the theme would update sizes and colors throughout the document.

The important limitation is that the existence of `measure` does not automatically make a fixed-height card safe from overflow. Measurement must use the actual column width and text context, and content must be measured before being constrained by a fixed-height wrapper. The component code should explicitly reject an overfull region.[^9]

**Assessment:** the cleanest match when the output is primarily a PDF and simplicity matters more than using a familiar web language. Build a small template, not a new publishing framework. Precise font matching and mixed-size baseline behavior remain things to demonstrate with an initial specimen.

### HTML/CSS and Chromium

This is the closest realization of the “document composed like a web app” idea. Components can be plain rendering functions or React components producing static HTML. The layout can use a fixed landscape sheet, two panel containers, and explicit columns within each panel. A full application framework or server is unnecessary.

Playwright's PDF API supports CSS page sizes, background printing, scale, and PDF output. Its defaults matter: CSS size preference and background printing are not enabled by default.[^10] A proposed print configuration is:

```css
@page { size: 11in 8.5in; margin: 0; }
.sheet {
  box-sizing: border-box;
  width: 11in;
  height: 8.5in;
  padding: var(--sheet-margin);
  break-after: page;
}
.sheet:last-child { break-after: auto; }
```

```js
// Illustrative configuration, not an implemented build script.
await page.emulateMedia({ media: "print" });
await page.evaluate(() => document.fonts.ready);
await page.pdf({
  path: "checklist.pdf",
  preferCSSPageSize: true,
  printBackground: true,
  displayHeaderFooter: false,
  scale: 1,
});
```

A row should have three logical regions: challenge, flexible leader, and response group. A dotted rule is easy, but it does not necessarily resemble the original period glyphs. A repeated-glyph or deliberately drawn leader allows more faithful control over spacing and baseline.

The browser makes debugging accessible: inspect boxes, baselines, font loading, and computed dimensions. However, DOM overflow checks alone are insufficient. Descendants can overlap without changing a container's scroll dimensions. Check row and region bounds, inspect the exported PDF, and assert that it has exactly two correctly sized pages.

**Assessment:** nearly as attractive as Typst, and preferable if a visual editor or interactive checklist is likely. Pin the browser and font assets. Do not assume that opening the HTML in a different browser and choosing Print produces the same artifact.

### Python and ReportLab

ReportLab offers both a PDF drawing canvas and Platypus, a layout system using flowables, frames, and document templates. Custom flowables supply sizing and drawing behavior.[^11][^12]

A small renderer could therefore implement a `ChecklistRow` that measures its label, qualifier, response, and note, reports its height, and draws the row. A section stacks rows; a column stacks sections. The outer sheet geometry can be fixed without hardcoding a y-coordinate for every item.

The advantage is control. Font metrics, line placement, borders, and table dimensions are explicit. The cost is implementing more details: mixed-font line layout, wrap decisions, baseline alignment, and accurate height calculations. Writing raw canvas commands for every item would be quick initially but expensive to maintain.

**Assessment:** a strong choice if explicit Python code feels more maintainable than a typesetting language. It is not inherently less capable of matching the reference; it simply puts more layout responsibility in the custom program.

### HTML/CSS and WeasyPrint

WeasyPrint provides a Python API and command-line HTML-to-PDF renderer. Its current documentation includes generated leaders and print-oriented features. Grid and flexbox support exist, with documented limitations; it would be inaccurate to dismiss it as having no grid support. Its documentation also cautions that renderer updates can alter layout even when the API remains compatible.[^13]

This is attractive for a Python-maintained project whose templates are HTML. Generate static HTML, then render it through WeasyPrint. Treat its PDF as the authoritative preview rather than expecting a browser preview to match exactly.

**Assessment:** worth choosing over Chromium when avoiding a browser runtime or using print-specific CSS is a priority. For the narrow mixed-size rows here, test the exact components before selecting it. The same CSS is not guaranteed to behave identically across the two engines.

### LaTeX with LuaLaTeX or XeLaTeX

TeX can express this layout with reusable commands, fixed panels, tabular structures, and leaders. `fontspec` provides OpenType font selection with LuaTeX/XeTeX, while `tcolorbox` supplies flexible framed boxes.[^14][^15]

For an experienced TeX maintainer, this is a dependable direction. For a new project with no language preference, package selection, macro syntax, escaping, and interactions between layout constructs create more conceptual overhead than the document needs.

**Assessment:** a credible solution, not the default recommendation here. Its mathematical typesetting strengths do not provide much additional value for this checklist.

### React PDF, pdfmake, and QuestPDF

`@react-pdf/renderer` uses components such as `Page`, `View`, and `Text`, with a documented CSS-like styling system and Flexbox support. It also supplies wrapping, orphan/widow, and hyphenation controls.[^16] It renders a PDF-specific component tree; it is distinct from a React page printed by Chromium. Choose it if that component model is especially appealing, but do not expect arbitrary HTML/CSS to carry over unchanged.

pdfmake defines documents as JavaScript objects, including columns with automatic, fixed, and proportional widths.[^17] That is conceptually close to the desired structured-content approach. It deserves a small specimen if a direct JavaScript PDF library is preferred, particularly to test mixed-size qualifiers and leaders.

QuestPDF supplies a compositional C# API.[^18] Its current Community License is source-available rather than OSI-approved open source, with eligibility conditions for free use.[^19] It is a reasonable .NET option, but there is little reason to introduce .NET solely for this document when Typst and HTML both fit.

### Paged.js, Vivliostyle, and commercial print engines

Paged.js paginates HTML in a browser for publication workflows. Vivliostyle CLI builds PDFs from HTML or Markdown and also supports other publication outputs.[^20][^21] These address the broader problem of paged web publishing. They become attractive for book-length checklists, running matter, or a publication series; this fixed two-page arrangement offers less reason to add their pagination layer.

Prince is a dedicated HTML/XML-to-PDF product. Its non-commercial license places a logo on generated output and has additional conditions; a commercial license is the relevant route for output without that logo.[^22] It merits consideration when dedicated print-engine support is valuable. For a personal two-page checklist, a recurring service or commercial engine is not necessary to meet the stated objective.

Pandoc is useful conversion infrastructure, but choosing it does not settle the rendering question: its PDF output delegates to a selected engine.[^23] A plain Markdown document also lacks the explicit checklist roles needed here. It is excellent for this research report, less compelling as the checklist's sole source language.

### Existing aviation editors and visual publishing tools

**EFIS Editor is an unusually relevant reference:** its documented model supports checklist groups and item types, exports printable PDFs with selectable page size, and retains a JSON representation. It also documents lossy mappings between different avionics/app formats.[^24]

There is a material applicability limit: its README explicitly restricts intended use to experimental aircraft and says certificated-aircraft use is not authorized. Therefore, I would use it as a design/reference lead, not recommend it as the production tool for this C172S. Its exact reproduction of the supplied table and two-panel layout has also not been demonstrated.[^24]

Garmin provides checklist-editing tools for supported avionics, and ForeFlight documents editing and sharing checklists.[^25][^26] These capabilities do not establish a general, programmable print layout or compatibility with every G1000 installation. If digital export becomes desirable, treat it as a separate output adapter with explicit capability checks.

Pages already proves that a visual authoring approach can achieve the target. More formal paragraph styles, table styles, and template discipline could improve consistency while retaining direct editing. A desktop-publishing application with scripting, such as Scribus, offers another hybrid route.[^27] The tradeoff is preserving a GUI document as the principal layout artifact and adding automation for semantic reuse.

## 4. A small, durable content model

Use a short list of block types rather than a generic document programming language. Most of this checklist can be represented by `check`, `note`, `branch`, `subprocedure`, `reference`, and `table`, contained in named procedures. Do not add arbitrary per-item coordinates or CSS until a real need exists.

The following is an illustrative schema, not a transcription or operational procedure:

```yaml
schema_version: 1
aircraft:
  model: "Cessna 172S"
  avionics: "G1000"
  applicability: "Record exact aircraft configuration here"

procedures:
  example:
    title: "EXAMPLE PROCEDURE"
    category: "normal"
    source_refs: ["source-to-be-recorded"]
    blocks:
      - type: "check"
        id: "example-step"
        challenge:
          - role: "panel-label"
            text: "EXAMPLE SWITCH"
          - role: "text"
            text: " position"
        qualifier: "example condition"
        response: "EXAMPLE RESPONSE"
        notes:
          - role: "explanation"
            text: "Example supporting information."

      - type: "branch"
        id: "example-branch"
        condition: "If the example condition applies"
        blocks:
          - type: "check"
            id: "example-branch-step"
            challenge: "Example control"
            response: "EXAMPLE ACTION"
```

Allow the common case to use plain strings; reserve arrays of inline runs for genuinely mixed semantics. No one should have to write a miniature syntax tree for every ordinary row.

Quote display strings such as `"ON"`, `"OFF"`, `"125.0"`, and `"1007'"`. YAML parsers differ in scalar interpretation, and frequency formatting must preserve trailing zeros. Store ordered steps in arrays, never in an unordered collection. A schema should catch duplicate IDs, missing fields, and invalid references.

### Where content should live

| Format | Strength | Weakness | Recommendation |
|---|---|---|---|
| YAML | Readable, comments, easy text diffs | Indentation and scalar interpretation | Default for checklist data |
| JSON | Strict, interoperable, many schema tools | More punctuation; no standard comments | Equally sound if tooling is the priority |
| Native Typst data/functions | Rich inline content, single toolchain | Couples authoring to Typst | Simplest alternative for a permanently Typst-only project |
| TypeScript objects | Editor types and reusable constructors | Requires a JS execution path | Natural for an HTML or React renderer |
| CSV/spreadsheet | Convenient flat rows and airport data | Poor representation of branches and nested notes | Use selectively for tabular reference data |
| Markdown alone | Easy prose editing | Checklist semantics become conventions embedded in text | Avoid as the primary checklist schema |

There is no need for a database, network service, or bespoke editor in the first version. A few local files and one repeatable build command are sufficient.

### Shared procedures and variants

Repeated placement should reference a procedure ID. Editing that procedure then changes every intended copy. However, the differing duplicates in the reference must first be classified as either accidental drift or intentional variants.

An intentional variant should have a name and an explicit relationship to its source, not a hidden rule such as “remove the last row if this is the left panel.” Named variants may share small groups, but avoid complicated inheritance chains. A straightforward resolved procedure is easier to review than a stack of patches.

Attach source metadata at procedure level by default, and at item level for adaptations or overrides. Useful fields include publication identifier, revision, section/page, applicability, and the reason for a personal addition. Keep this information in a review view or source file so it does not overwhelm the printed card.

Airport data should have its own source and effective-date fields. Its update cadence differs from the procedures. The existing values have been observed as layout content only; this report does not establish their current accuracy.

## 5. Page placement and styling

Use **explicit placement of sections with automatic layout inside each section**. That is the useful middle ground between individually positioned text and unpredictable whole-document reflow.

An illustrative placement description is:

```yaml
paper: "letter-landscape"
sides:
  - id: "emergency-side"
    left_panel:
      upper_columns:
        - ["takeoff-engine-out", "after-takeoff-engine-out", "flight-engine-out-variant"]
        - ["ditching", "after-landing", "shutdown-variant"]
      lower_span: "airport-information"
    right_panel:
      columns:
        - ["flight-engine-out", "landing-with-power", "landing-no-power", "engine-fire"]
        - ["start-fire", "electrical-fire"]
```

These IDs describe placements suggested by the original, not approved procedures. The same content can later be placed in another layout without modifying its wording.

Theme settings should include body/header/note/qualifier fonts and sizes, row spacing, note spacing, bar padding, border widths, leader pitch, panel gutter, section gap, and normal/emergency colors. Derive column widths from sheet and gutter dimensions. Do not store dozens of near-identical numbers copied from the Pages export.

Font availability is part of the build configuration. For a close local match, identify the actual Helvetica and Helvetica Neue faces used by Pages and select them explicitly. For a portable project, choose font assets that can be distributed with the project, or document the required local fonts. A substitute with a similar appearance can still have different character widths and change many rows. The subset fonts embedded in the existing PDF should not be treated as a complete reusable font library.

Changing paper size is mechanically easy. Preserving usability at a smaller size is not. A new paper size should trigger a new fit check and potentially a different placement profile; it should not simply scale down the current sheet.

### Row layout and overflow behavior

A renderer should apply a documented sequence:

1. Measure the challenge and response group, including the qualifier, in their actual fonts.
2. If both fit with a minimum leader gap, use one line.
3. Otherwise use an approved multiline arrangement that keeps the response clearly associated with its challenge.
4. Keep a note with its parent and a branch heading with its first action.
5. Report region overflow with the affected procedure and measured excess.

Prefer a diagnostic such as `Starting Engine exceeds right-panel column by 13 pt` over silent clipping, hidden overflow, ellipses, or type shrinking. The exact diagnostic mechanism will depend on the chosen engine.

Disable automatic hyphenation for cockpit labels and action values. Preserve nonbreaking relationships for units and short settings where practical. Those protections can themselves cause overflow, which is why measuring and reporting fit is part of the renderer's job.

For close visual matching, leader styling deserves attention. Ordinary periods, ellipsis characters, and a dotted vector line have different spacing and shapes. The content should contain none of them; the component should produce one consistent leader treatment, with no collision against either text edge.

## 6. Scope of a first implementation

A sensible initial project would have a structure like this:

```text
content/
  procedures.yaml
  airports.yaml
  sources.yaml
layout/
  letter-landscape.yaml
theme.typ
components.typ
main.typ
README.md
```

This is a proposed structure, not files created by this report. Under an HTML implementation, the Typst files would become component/template code, print CSS, and a PDF build script. A separate validation script is optional if the chosen renderer can perform the required checks clearly.

The custom work is bounded: data loading, a handful of components, explicit placement, and validation. Hundreds of lines rather than an application platform is a plausible initial scale, but a precise estimate would depend on wrapping requirements and desired diagnostics. Exact visual tuning and transcription review are likely to require more care than basic PDF generation.

### A focused proof before committing

The first implementation should render a **representative specimen**, not begin by migrating every line. Include a long label, long response, 6 pt qualifier, two-line italic note, conditional box, nested group, emergency heading, and a small airport table. Include an intentionally overfull column.

Compare that specimen at actual size against the relevant regions of the original. The decision criteria are:

| Criterion | Successful result |
|---|---|
| Font fidelity | Intended fonts and weights; no silent substitutions |
| Paired rows | Stable right alignment and readable leaders at several text lengths |
| Mixed-size text | Qualifiers align predictably with the action |
| Branches and notes | Scope and attachment remain obvious |
| Fit behavior | Overflow produces an actionable failure |
| Maintainability | One style edit updates all specimen instances |
| Portability | Build succeeds with documented local dependencies |

Start with Typst. If its mixed-inline layout or fit diagnostics require awkward workarounds, reproduce the same specimen with HTML/Chromium and compare. There is little value in building full implementations in several engines before resolving those representative cases.

### Migration and verification

Once the specimen is satisfactory, transcribe the complete content while retaining the original as the visual reference. Review duplicate variants explicitly. PDF extraction can accelerate transcription, but it interleaves columns and leaders and is not a reliable source of procedure structure.

Verification should address separate questions:

* **Content:** Every expected step, response, qualifier, and note is present, in order, with intentional repeated placements accounted for. The applicable POH, supplements, and school adaptations need a distinct content review.
* **Geometry:** Exactly two 792 × 612 pt pages for the reference profile; no clipped rows, unexpected page breaks, missing fonts, or intrusions into the central gutter.
* **Appearance:** Render both PDFs at the same resolution for side-by-side inspection or overlays. Pixel differences alone are insufficient because antialiasing can differ, and a visually identical page can still contain incorrect words.
* **Editing behavior:** Lengthen a response, add a note, and increase type size to verify that the renderer wraps or reports overflow as intended.
* **Physical output:** Print at 100% and confirm edge clearance, duplex orientation, and the intended fold/cut arrangement. Printer feed conventions vary, so use a labeled duplex proof rather than assuming a flip setting.

Keep a short revision identifier on each physical panel if panels may be separated. Retain a build manifest with content revision, theme revision, compiler/browser version, and font identities. The goal is reproducible layout and explainable changes, not necessarily byte-for-byte identical PDF metadata.

## 7. Recommended choice

**Choose Typst with YAML content, an explicit placement file, and a compact component library** if the primary artifact remains a carefully typeset personal PDF. This best matches the current preference for fit and simplicity without a language commitment.

Choose **HTML/CSS with Playwright/Chromium** instead if browser-based editing, interactive previews, or reuse in a web interface becomes a near-term priority. React can help organize components, but is optional.

Choose **ReportLab** if straightforward Python measurement and drawing code is the most comfortable maintenance model. Choose **LaTeX** if existing TeX expertise outweighs the learning cost. The other approaches are credible, but none currently has a project-specific advantage strong enough to displace those choices.

Before optimizing fidelity, settle how to handle the original's size-versus-density tradeoff and differing duplicate procedures. The publishing system should make those decisions explicit and reversible. It should preserve the checklist's familiar organization while making content changes and style changes independently reviewable.

## Sources

Web documentation and product terms were consulted in September 2026. Historical aviation reports are identified by their publication dates, not search-engine crawl dates. Assessments of fit, proposed architecture, and implementation scope are original analysis; source citations substantiate the underlying features or guidance.

[^1]: Supplied local artifact, `original.pdf`, two pages, exported from Apple Pages. PDF title: “C172S G1000 V2.” Both pages visually inspected; dimensions, font spans, and graphical coordinates extracted. This source establishes the reference design, not procedure authority.

[^2]: Asaf Degani and Earl L. Wiener. _Human Factors of Flight-Deck Checklists: The Normal Checklist_. NASA CR-177549, May 1990. [FAA-hosted report](https://www.faa.gov/sites/faa.gov/files/2022-11/NASA%20Ames%20Rpt%20CR%20177549%20.pdf), especially §3.1.4, discussion of checklist methods, printed pp. 18–19.

[^3]: Asaf Degani. _On the Typography of Flight-Deck Documentation_. NASA CR-177605, December 1992. [Report hosted by SINTEF](https://www.sintef.no/globalassets/project/hfc/documents/nasa-typography-flight-deck_documentation.pdf), §2, §3.4, and §6. The original NASA download endpoint was inaccessible; the cited copy contains the original report.

[^4]: UK Civil Aviation Authority. _Guidance on the Design, Presentation and Use of Emergency and Abnormal Checklists_, CAP 676, Issue 3, August 30, 2006. [Official report](https://www.caa.co.uk/publication/download/12202), Chapter 7, especially §§1.5–1.9 and 2.8–2.10. The [CAA publication catalog](https://www.caa.co.uk/data-and-publications/publications/publication-categories/airline-operations/) lists CAP 676 as current.

[^5]: Federal Aviation Administration. _AC 120-71B: Standard Operating Procedures and Pilot Monitoring Duties for Flight Deck Crewmembers_, January 10, 2017. [Official status and scope](https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/1030486); [full circular](https://www.faa.gov/documentlibrary/media/advisory_circular/ac_120-71b.pdf).

[^6]: Typst GmbH. [Open Source](https://typst.app/open-source/). Compiler licensing, local use, and distinction from the commercial web application.

[^7]: Typst documentation. [Grid](https://typst.app/docs/reference/layout/grid/), [Repeat](https://typst.app/docs/reference/layout/repeat/), and [Table](https://typst.app/docs/reference/model/table/). Layout and leader primitives.

[^8]: Typst documentation. [YAML](https://typst.app/docs/reference/data-loading/yaml/). Structured input and type conversion.

[^9]: Typst documentation. [Measure](https://typst.app/docs/reference/layout/measure/). Context, available dimensions, and measured versus constrained content.

[^10]: Microsoft Playwright documentation. [Page.pdf](https://playwright.dev/docs/api/class-page#page-pdf). Print media, PDF sizing, scale, and background options.

[^11]: ReportLab documentation. [Chapter 5: Platypus](https://docs.reportlab.com/reportlab/userguide/ch5_platypus/) and [Chapter 2: Graphics and text with pdfgen](https://docs.reportlab.com/reportlab/userguide/ch2_graphics/).

[^12]: ReportLab documentation. [Chapter 10: Writing Your Own Flowables](https://docs.reportlab.com/reportlab/userguide/ch10_writing_own_flowables/).

[^13]: CourtBouillon. [WeasyPrint API Reference](https://doc.courtbouillon.org/weasyprint/stable/api_reference.html), versioning, Python API, generated content, and CSS grid/flexbox support. Consult the documentation matching the pinned implementation version.

[^14]: CTAN. [fontspec](https://ctan.org/pkg/fontspec). Font selection in XeLaTeX and LuaLaTeX.

[^15]: CTAN. [tcolorbox](https://ctan.org/pkg/tcolorbox). Framed and colored content boxes.

[^16]: React-pdf maintainers. [Styling](https://react-pdf.org/docs/v4/styling) and [Advanced features](https://react-pdf.org/docs/v4/advanced). Refers to `@react-pdf/renderer`.

[^17]: pdfmake documentation. [Columns](https://pdfmake.github.io/docs/0.3/document-definition-object/columns/). Document-definition objects and sizing choices.

[^18]: QuestPDF. [Quick start](https://www.questpdf.com/quick-start.html). C# document composition.

[^19]: QuestPDF. [Community License](https://www.questpdf.com/license/community.html), version 3.0, effective July 6, 2026. Current source-available terms and eligibility; older descriptions of its licensing can differ.

[^20]: Paged.js. [The big picture](https://pagedjs.org/en/documentation/1-the-big-picture/). Browser-based paged publication workflow.

[^21]: Vivliostyle. [CLI: Getting Started](https://docs.vivliostyle.org/en/cli/getting-started/). HTML/Markdown input and publication output.

[^22]: Prince. [Documentation](https://www.princexml.com/doc/) and [License FAQ](https://www.princexml.com/purchase/license_faq/), especially non-commercial output restrictions.

[^23]: Pandoc. [User's Guide](https://pandoc.org/MANUAL.html), PDF creation and `--pdf-engine`.

[^24]: Rafael Damazio and contributors. [EFIS Editor repository and README](https://github.com/rdamazio/efis-editor), supported formats, PDF printing, JSON storage, and intended-use disclaimer. Feature descriptions are the project's claims; exact-layout suitability was not tested.

[^25]: Garmin. [Creating or Updating a Checklist](https://support.garmin.com/en-ZA/aviation/faq/3P2QnpxP7NAMDUk6Ig6kpA/). Availability of Garmin checklist-editing programs; not a compatibility determination for the particular aircraft.

[^26]: Jeppesen ForeFlight. [_ForeFlight Checklist Guide_, version 18.1.1, February 2026](https://cloudfront.foreflight.com/docs/ff/18.1.1/ForeFlight%20Checklist%20Guide.pdf), checklist creation/editing and sharing sections.

[^27]: Scribus project. [Get Started With Scribus](https://wiki.scribus.net/wiki/images/0/08/ScribusTutorial.pdf). Visual publishing and Python scripting.
