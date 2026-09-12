# Text-size experiment

> Historical research and experiments. Implementation claims, commands, file paths, and page counts describe the experiment at the time. The comparison layouts were retired during repository cleanup; commit `9174e4a` preserves their last implementation. See the [README](../README.md) for the maintained document.

The straightforward size increase does not fit the former two-page layout, even after removing the airport table. Two complete comparison PDFs are now buildable. Their page counts describe these layouts, not proven minimum page counts.

## Size policy

[CAA CAP 676, Chapter 7 §1.6](https://www.caa.co.uk/publication/download/12202) recommends approximately 12 pt normal text and 14 pt headings, with respective minima of 10 pt and 12 pt, evaluated at about 600 mm. These are contextual human-factors recommendations, not certification of this document's readability.

The recommended profile uses **12 pt for actions, notes, qualifiers, branch titles, and page footers**, and **14 pt for section headings**. The minimum profile uses **10 pt throughout the body** and **12 pt headings**. No small-font exception is used to squeeze notes or conditions into either layout. Existing italic/weight distinctions remain for this experiment; their semantic review is a separate task.

## What broke in the former arrangement

The old layout had 189 pt columns and 594 pt of vertical space. Removing the airport table gave that full height to all eight columns. A direct increase first failed because multiple section titles were wider than their headers.

After allowing headings to wrap and grow, the following natural column heights were measured in Typst. This experiment used the recommended profile's 24 pt minimum header height, 4.5 pt row gaps, 3 pt attached-note gaps, and 8 pt section gaps.

| Former position | Content | Needed | Available | Excess |
|---|---|---:|---:|---:|
| Emergency, column 1 | Takeoff/after-takeoff/short flight engine-out | 530.6 pt | 594 pt | Fits |
| Emergency, column 2 | Ditching | 183.1 pt | 594 pt | Fits |
| Emergency, column 3 | Full engine-out, two landings, engine fire in flight | 1003.3 pt | 594 pt | 409.3 pt |
| Emergency, column 4 | Engine-start fire, electrical fire | 762.1 pt | 594 pt | 168.1 pt |
| Normal, column 1 | After start, run-up, before takeoff | 980.3 pt | 594 pt | 386.3 pt |
| Normal, column 2 | After takeoff through shutdown | 951.4 pt | 594 pt | 357.4 pt |
| Normal, column 3 | Cabin/empennage/right wing/nose preflight | 1029.1 pt | 594 pt | 435.1 pt |
| Normal, column 4 | Left wing/before start/starting engine | 961.4 pt | 594 pt | 367.4 pt |

Six of eight columns overflow; the worst needs about 73% more height. This includes the effect of keeping notes and qualifiers readable and letting headers grow, not just enlarging the main rows. Narrow columns also move many responses onto a separate line. Removing the table helps only the emergency side, so it cannot solve the normal side's density.

## Complete comparison layouts

| Profile | Font sizes, body/header | Paper and columns | Pages | Main tradeoff |
|---|---|---|---:|---|
| Recommended | 12/14 pt | Portrait Letter, two 288 pt columns | 5 | Larger text and mostly single-line action/response pairs; more pages |
| Minimum | 10/12 pt | Landscape Letter, four 189 pt columns | 3 | Fewer pages; more wrapped headings, responses, and notes |

The recommended version contains two emergency pages and three normal pages. Normal procedures now follow chronological reading order: preflight, start, run-up/takeoff, cruise/approach/landing/shutdown. The minimum version contains one emergency page and two normal pages.

Both profiles keep each procedure intact, retain all 26 procedure placements (25 canonical procedures plus the shorter engine-out variant), omit the airport table, and show page numbers and the font-size profile in their footers. The shorter and longer engine-out copies remain separate pending content QA.

The airport dataset remains in `content/airports.yaml` as reference material; the renderer no longer contains table code. The preceding 8 pt PDF is preserved at `tmp/comparison/checklist-before-text-size.pdf`.

## Options for the next layout pass

1. **Develop the 12/14 pt portrait version.** It gives the clearest view of the intended size increase. Its white space is partly a result of keeping procedures intact, keeping emergency and normal pages separate, and preserving chronological normal flow. This first layout does not attempt global page-count minimization.
2. **Use the 10/12 pt comparison as a compactness baseline.** It uses the stated minimum sizes, not the preferred sizes. Narrow-column response wrapping remains a significant visual difference from the original.
3. **Explore tighter packing at 12/14 pt.** Allowing normal and emergency material to share a page, or changing column counts, may reduce page count. Splitting long procedures would need deliberate continuation labels and a separate usability decision. No smaller-page-count claim has been validated here.
4. **Explore a larger physical sheet or a card set.** More printable area or a different physical organization may help, but changing paper size alone is not proof of cockpit usability. Evaluate holding, stowage, and navigation at actual size.
5. **Revisit content only during content QA.** Resolving the remaining engine-out duplication or separating instructional material from the operational checklist may save space. No procedure wording or steps were shortened to make these layouts fit.

## Reproduce and verify

```sh
make build       # output/pdf/checklist.pdf: 12/14 pt recommended profile
make minimum     # output/pdf/checklist-minimum.pdf: 10/12 pt comparison
make watch       # watch the recommended profile
make test        # both profiles and renderer failure cases
```

All 17 tests passed for the initial two profiles. All eight output pages were rendered and visually inspected. Print each comparison at 100% / actual size; Fit-to-page scaling would invalidate the size comparison.

## Physical-format comparison

This section records the initial comparison. Its half-Letter counts and print grouping are superseded by the [kneeboard refinement](#kneeboard-refinement) below.

Following the format research, the printing constraint was relaxed to include common print-shop sizes. The four additional outputs keep 12 pt actions, notes, qualifiers, and footers; 14 pt headings; the same row/section spacing; and all 26 procedure placements. None splits a procedure. Normal reading order remains chronological.

All four use 0.25 in top/side margins, a 0.5 in bottom margin for the footer, and 0.25 in gutters where applicable. The smaller-page footers omit the redundant type-size label to fit at 12 pt. These margins are for the format comparison; a chosen binding or lamination border may need additional allowance.

| Profile / output | Finished page size | Columns | PDF sides | Emergency / normal sides | Physical sheets or leaves* |
|---|---|---|---:|---|---:|
| `checklist-half-letter.pdf` | 5.5 × 8.5 in portrait | 1 | 13 | 5 / 8 | 7 |
| `checklist-reference-card.pdf` | 6.5 × 9 in portrait | 1 | 12 | 4 / 8 | 6 |
| `checklist-legal.pdf` | 8.5 × 14 in portrait | 2 | 4 | 2 / 2 | 2 |
| `checklist-tabloid.pdf` | 17 × 11 in landscape | 4 emergency; 3 normal | 3 | 1 / 2 | 2 |

*Assumes duplex printing, keeping emergency and normal material on separate physical sheets/leaves. Counts refer to finished pieces, not the larger stock used for printing and trimming. For half-Letter, print pages 1–5 as one duplex group (last reverse blank) and pages 6–13 as another. For reference cards, the groups are 1–4 and 5–12. For Legal, pages 1–2 form the emergency sheet and 3–4 the normal sheet. For Tabloid, print page 1 on a single-sided emergency sheet and pages 2–3 on a double-sided normal sheet. Blank reverse sides are not included as pages in the PDFs.

These are deliberately grouped layouts, not proven minimum page counts. Sparse pages arise from keeping procedures intact and normal phases in order. For example, the roughly 476 pt Starting Engine procedure cannot share a 558 or 594 pt column with Before Starting Engine or After Start. Extra width alone does not solve that vertical boundary.

### What the comparison suggests

**Legal is the leading larger-sheet candidate.** Normal procedures fit on one double-sided sheet: preflight/start on the front, after-start through shutdown on the back. Emergency procedures occupy another double-sided sheet. It reduces the five-page Letter baseline to four sides with unchanged type sizes and more generous outer margins. Its 14 in height still needs a physical handling check.

**Tabloid provides a single emergency face**, but normal procedures still occupy two faces in this arrangement. It therefore takes the same two physical sheets as Legal, at a larger size. It may be useful if seeing all emergency sections at once is especially valuable; fewer PDF pages alone is not a reason to prefer it.

**The small formats are portable but need a page-navigation design.** The 6.5 × 9 in card version saves one emergency face relative to half-Letter, while both require eight normal faces. Some pages have long leaders and substantial white space: more width does not reduce height once the rows already fit on one line. They are content-layout proofs for a possible card stack or book, not finished tabbed or ring-punched products.

My current recommendation is to physically compare Legal against the 6.5 × 9 in cards before choosing a permanent format. A smaller book remains viable if portability matters more than the number of leaves. Content QA may change all these counts; the remaining engine-out duplication is still preserved.

### Print-shop considerations

[FedEx Office lists Letter, Legal, and Tabloid as standard document sizes](https://www.office.fedex.com/default/document-printing), with finishing options varying by product. The card sizes would be printed on larger stock and trimmed. Actual lamination, trimming, finish, and binding choices should be agreed with the local shop after selecting the format; this comparison does not assume that every size/finish combination is available online.

Supply the selected PDF at actual size. Ask for a physical proof before the final laminated set so the finished dimensions, duplex orientation, and readability can be evaluated. Any lamination extending beyond the paper adds to its finished footprint. These files do not include crop marks, bleed, binding holes, tabs, or folding/hinge construction.

### Build and verification

`make formats` builds all four PDFs in `output/pdf/`. An individual output can be rebuilt with, for example, `make output/pdf/checklist-legal.pdf`. The existing `make build` and `make minimum` baselines remain available.

The existing 17-test suite now covers all six profiles: exact page counts and dimensions, actual font sizes, embedded fonts, text bounds, procedure completeness and order, comparison against the original PDF, and renderer failure cases. All pass. All 32 new output pages were rendered and visually inspected, including headers, notes, branches, and footers. Procedure content files were not edited for this experiment.

## Kneeboard refinement

This section records the six-card 12/14 pt version, retained for comparison. The current candidate is the [three-card version](#three-card-comparison) below.

The current target is a 5.5 × 8.5 in portrait card that can be used on a conventional kneeboard. This supersedes the earlier recommendation of unfolded Legal sheets. `output/pdf/checklist-half-letter.pdf` now contains **12 sides, paired as six duplex cards**, rather than 13 sides needing seven physical cards with a blank reverse.

### Changes

- Retained 12 pt body, notes, qualifiers, and footer text, plus 14 pt procedure headings.
- Reserved the top 0.5 in as a blank clip area, up from 0.25 in. Side margins remain 0.25 in. The clip allowance is a design starting point; the actual clip still determines fit.
- Reduced row gaps from 4.5 to 3 pt and attached-note gaps from 3 to 2.5 pt. Section gaps, header heights, and boxed-group padding remain unchanged.
- Added card identifiers E1/E2 and N1–N4, A/B side labels, subjects, aircraft identification, and the reverse-side identifier. Each pair occupies consecutive PDF pages.
- Reorganized the emergency pages to fit four sides. Normal procedures remain in chronological order across eight sides. Every procedure and both engine-out versions remain complete and unchanged.

| Card | Side A | Side B |
|---|---|---|
| E1 | Takeoff/after-takeoff/brief in-flight engine-out; ditching | Full in-flight engine-out; landing without power |
| E2 | Engine fires in flight and during start | Electrical fire; landing with power |
| N1 | Cabin and empennage preflight | Right-wing and nose preflight |
| N2 | Left-wing preflight; before starting | Starting engine |
| N3 | After start | Run-up |
| N4 | Before/after takeoff, cruise, approach | Before/after landing, shutdown |

The E2-B pairing uses the remaining space for Landing With Power. It is a separate procedure under its own header, not an added step in Electrical Fire. This grouping is a space/navigation tradeoff worth assessing during the physical review.

Some normal sides remain sparse, especially After Start. Pairing it with Run-Up on the reverse creates a useful taxi/run-up card without splitting either procedure. At this spacing, Starting Engine requires about 439 pt and After Start about 212 pt: their combined 660 pt including the section gap exceeds the 540 pt content area. Further substantial reductions need different content decisions or deliberate procedure continuations, rather than merely wider rows.

### Compare and print

The previous 13-side PDF is preserved unchanged at `tmp/comparison/checklist-half-letter-before-kneeboard.pdf`. Build that version with `make output/pdf/checklist-half-letter.pdf`.

Print at actual size, pairing pages 1/2, 3/4, 5/6, 7/8, 9/10, and 11/12. There are no intentional blank sides. For flipping cards over their top edge, request short-edge duplex; for turning them sideways like a book, use long-edge duplex. Have the shop verify an A/B proof before printing and laminating the set. These are finished paper dimensions; any clear lamination border will increase the outside footprint. This PDF is not an imposition on larger stock and does not include tabs or punched-binding allowances.

All 18 tests pass across all six profiles, including original-PDF transcription and a new check for card pairing, category separation, and blank clip space. All 12 revised sides were rendered and visually checked. This remains a layout revision; procedure content QA is still pending.

## Three-card comparison

The six-card version proved too cumbersome for the user's intended handling. The next comparison, `output/pdf/checklist-kneeboard-compact.pdf`, fits all content on **six sides: three double-sided 5.5 × 8.5 in cards**. The preceding six-card PDF remains at `output/pdf/checklist-half-letter.pdf`.

### Typography and geometry

- 10 pt actions, responses, qualifiers, notes, and footers; 12 pt procedure headings. No smaller supporting-text exceptions.
- Two 174 pt columns separated by a 12 pt gutter; 18 pt side margins.
- The same blank 36 pt (half-inch) top clip area and 36 pt bottom footer region as the larger-text cards. Each column has 540 pt of content height.
- 3 pt row gaps, 2 pt attached-note gaps, and 3 pt component insets. Section gaps remain 8 pt and minimum heading height is 22 pt. Long headings grow and long responses wrap without shrinking.

This profile uses the earlier 10/12 pt theme with explicit spacing overrides; the existing larger-text and other physical-format profiles are unchanged.

### Card arrangement

Read down the left column, then down the right. Consecutive PDF pages are opposite sides of one card.

| Card | Side A | Side B |
|---|---|---|
| N1: preflight/start | Cabin, empennage, right wing, nose | Left wing, before starting, starting engine |
| N2: normal flight | After start, run-up | Before/after takeoff, cruise, approach, before/after landing, shutdown |
| E1: emergencies | Takeoff/after-takeoff/brief in-flight engine-out; full in-flight engine-out, landing without power, ditching | Engine fires, electrical fire, landing with power |

Before Takeoff begins N2-B because putting it beneath Run-Up would overfill that column at the chosen width and spacing. The normal sequence is still chronological. Some columns remain sparse because each procedure stays intact; no words, steps, notes, or variants were removed to meet the card count.

The main compromise is narrower lines. More challenges and responses occupy separate lines, and notes and some headings wrap. E1-A's landing/ditching column is particularly full, with little remaining room for additions. This is a complete layout to judge at actual size, not a claim that it achieves the same reading ease as the larger-text cards.

### Build, print, and verify

`make output/pdf/checklist-kneeboard-compact.pdf` builds this three-card comparison. `make output/pdf/checklist-half-letter.pdf` builds the six-card comparison. The Letter baseline can be built with `make output/pdf/checklist-recommended.pdf`.

Print at 100% / actual size, pairing pages 1/2 (N1), 3/4 (N2), and 5/6 (E1). For a top-edge flip use short-edge duplex; for a book-style side flip use long-edge duplex. The shop can arrange these finished-size pages on larger stock and trim them without scaling. The PDF itself is not an imposed printing sheet. Lamination borders add to the finished footprint.

All 18 tests pass across seven profiles. They check exact dimensions and font sizes, embedded fonts, full procedure content and order, transcription against the original PDF, card pairing/category separation, clip clearance, and layout failure cases. All six compact sides were rendered and visually inspected. Procedure content QA remains pending.

## Return to original font sizes

The user found three cards still too cumbersome and chose to restore the original type sizes while retaining the new footers. The current default, `output/pdf/checklist.pdf`, now contains **four sides: two double-sided 5.5 × 8.5 in cards**. Build it with `make build` or `make kneeboard`; its explicit profile is `kneeboard-original`.

- Checklist items: 8 pt; section headings: 9 pt; notes: 7 pt; qualifiers: 6 pt.
- Card/side and reverse-side footers remain 10 pt.
- Two 174 pt columns, a 12 pt gutter, 18 pt side margins, and 36 pt top/bottom regions retain the preceding card geometry.
- Original component dimensions are restored: 14 pt minimum headers, 3.5 pt insets, 2.5 pt note gaps, and 6 pt section gaps. Row gaps are tightened from the original 3.5 pt to 2 pt.

At the original row spacing, the four normal columns would require approximately 592, 581, 575, and 570 pt, exceeding the 540 pt available. At 2 pt row spacing, they require approximately 530, 519, 517, and 521 pt. No procedure is split, shortened, or omitted to achieve this.

| Card | Side A | Side B |
|---|---|---|
| N1 | All preflight sections, before starting, starting engine | After start, run-up, before/after takeoff, cruise, approach, before/after landing, shutdown |
| E1 | Takeoff/after-takeoff/brief and full in-flight engine-out, landing without power, ditching | Engine fires, electrical fire, landing with power |

Print at actual size, pairing pages 1/2 and 3/4. These remain finished-size card pages for the shop to arrange on larger stock if needed. The emergency card has more spare space than the normal card; the typography and spacing are consistent across both.

The three-card 10/12 pt comparison remains in `output/pdf/checklist-kneeboard-compact.pdf`. The previously default five-page Letter PDF is preserved at `tmp/comparison/checklist-before-original-size-return.pdf`.

All four current sides were rendered and visually inspected. The existing 18 tests now cover eight profiles, including the new card count, original text sizes plus 10 pt footers, content preservation, pairing, and clip clearance. Procedure content QA remains pending.

## Equal top margins and selective vertical stretching

The current profile now uses 18 pt (¼ in) top and side margins, retaining the 36 pt bottom region and existing footers. Its columns were initially 558 pt high; the footer-spacing refinement below reduces their stretch target. Columns naturally filling at least 90% of that height expand their line spacing and vertical component gaps proportionally to reach the bottom. Font sizes, widths, and internal box padding stay fixed; spacing expansion is capped at 2×. The four normal columns now align at the bottom of their content regions. Both emergency pages keep their natural spacing. The earlier clip-clearance geometry above records the preceding experiment.

The added 3 pt external margins around inline boxes participate in this spacing adjustment. All four sides were visually inspected, and the render tests now check aligned normal-column baselines and unstretched sparse emergency pages alongside content and margin checks.

## Footer separation

The stretch target now reserves a separate 12 pt buffer above the existing footer region, reducing each column’s available height to 546 pt. The normal columns end at 564 pt from the top of the page. The footer position, 36 pt bottom margin, 18 pt top/side margins, type sizes, and sparse emergency-page spacing remain unchanged. The render check also requires at least 12 pt of visible clearance between checklist text and footer text.

## Consolidated in-flight engine-out procedure

Page 3 now places the complete Engine Out - During Flight procedure below the takeoff and after-takeoff procedures in the left column. The shorter duplicate is no longer placed in the current document. The complete procedure retains every item and note, including the final FUEL PUMP OFF item. Landing without power and ditching remain in the right column. The current document therefore contains 25 complete procedures, each placed once; earlier comparison layouts still retain the source’s shorter copy.
