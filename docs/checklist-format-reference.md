# Flight-checklist format references

> Historical research and experiments. Implementation claims, commands, file paths, and page counts describe the experiment at the time. The comparison layouts were retired during repository cleanup; commit `9174e4a` preserves their last implementation. See the [README](../README.md) for the maintained document.

Research date: September 12, 2026. Scope: physical formats and page organization to guide the next C172S checklist layout. This supplements `research.md` and `text-size-study.md`.

## Finding

The reviewed sources show several established formats, not one universal GA checklist template. Commercial products demonstrate practical card and booklet sizes; manufacturer and school PDFs demonstrate page organization; human-factors guidance supplies evaluation criteria. These are different kinds of evidence. A published example is not proof that its typography is ideal, nor evidence of how many pilots use that format.

For this project, choose the **finished object held in the cockpit** before choosing how many Letter sheets it occupies. Printing two smaller pages on a sheet is a separate production decision. Shrinking an already composed PDF reduces its type size; composing smaller pages at 12 pt does not.

## Concrete reference set

| Reference | Verified format | Useful reference feature |
|---|---|---|
| [CheckMate product range](https://www.checkmateaviation.com/pages/our-products) | Standard 6.5 × 9 in; Compact 5 × 7 in. Classic CheckMate is a single-card product. | A compact reference-card approach; finished size is independent of standard printer paper. |
| [Qref cards](https://qref.com/) | Two double-sided 5 × 8 in cards: normal and emergency. Matte laminate. | Separating categories across cards gives four usable faces. |
| [Qref books](https://qref.com/) | 4.5 × 8 in, tabbed, bound, synthetic pages with a matte finish. | A small book is an established alternative when comprehensive material exceeds card capacity. |
| [Diamond DA40 TDI A5 checklist](https://www.diamondaircraft.com/fileadmin/diamondaircraft/service-and-support/Pilot_Training_Austria/Checklists/checklists_DA40_D/DA40_D_Conventional_Cockpit/DA40_TDI_Checklist_Edit17_1_A5.pdf) | Edition 17.1, April 15, 2017. Ten landscape A4 PDF sheets, each containing two smaller page panels. | Concrete manufacturer example of A5 pages arranged two per printing sheet. |
| [University of Oklahoma Cessna A-152 checklist](https://ou.edu/content/dam/ags/aviation/documents/resources/checklists/cessna-75.pdf) | Document dated December 12, 2019. Four landscape Letter PDF sheets containing eight individually numbered panels. | A school example of approximately half-Letter panels with chronological normal procedures and separate emergency material. |
| [FAA-sponsored *Checklist Guidelines* study](https://www.faa.gov/sites/faa.gov/files/2022-11/VNTSC%20Rpt%20DTO-VNTSC-FAA-91-7.pdf) | Historical 1991 research explicitly discusses a laminated or trifold Letter normal-checklist card. | An established folded-sheet approach and an explanation of the handling cost of page turning. |

Qref's [Cessna 172S book listing](https://qref.com/Cessna-172S-Skyhawk-SP-Multi-Page-Qref-Checklist_p_42.html) specifies 38 pages, demonstrating that a small aircraft checklist product can be substantially longer than two faces. That particular listing is for an analog cockpit, not our G1000 configuration. The reference here is its physical format, not its procedures.

Diamond's [official checklist directory](https://www.diamondaircraft.com/en/service-and-support/diamond-flight-training/checklists/) offers both A4 and A5 paper versions for conventional DA40s, and paper/electronic packages for several G1000 aircraft. The files are still published there, but their edition dates should not be confused with the research date.

## What the actual PDFs show

I inspected the PDF geometry, extracted text sizes, and rendered the normal-procedure sheet in each of the two downloadable examples.

**Diamond:** the A5 download has an approximately 842 × 595 pt PDF page, with two portrait panels. Its normal-procedure example uses numbered challenge/response rows, dotted leaders, shaded check blocks, separate procedure text, completion markers, and revision/page footers. On PDF sheet 3, the main Verdana rows measure approximately 11 pt; much italic supporting text measures about 8.3 pt. Its separation of check blocks and supporting procedures is useful to study, but the smaller text and italic actions are not a typography policy to adopt wholesale. [Diamond PDF](https://www.diamondaircraft.com/fileadmin/diamondaircraft/service-and-support/Pilot_Training_Austria/Checklists/checklists_DA40_D/DA40_D_Conventional_Cockpit/DA40_TDI_Checklist_Edit17_1_A5.pdf)

**Oklahoma:** the PDF measures 792 × 612 pt: landscape Letter. Each half has its own page number and footer. PDF sheet 3 places pre-taxi/run-up/before-takeoff on the left and subsequent flight phases on the right. Colored header bars, dotted leaders, and conditions in headings aid organization. Main rows on that sheet measure about 9 pt in Times New Roman. This is a useful reference for phase grouping and two-panel printing, not a match for our 12 pt objective. The PDF does not establish the school's exact cutting or binding practice. [Oklahoma PDF](https://ou.edu/content/dam/ags/aviation/documents/resources/checklists/cessna-75.pdf)

These are measured PDF text sizes at 100% scale, not measurements of perceived character height. The commercial product pages do not provide enough typography specifications to verify their printed font sizes.

## Guidance to apply across formats

[CAA CAP 676, Chapter 7](https://www.caa.co.uk/publication/download/12202), issued August 30, 2006, evaluates emergency and abnormal checklists by cockpit use rather than prescribing one paper size. Its relevant recommendations include:

- Fit the available workspace and stowage; avoid obstructing controls or displays.
- Allow a bound checklist to fold back through 360 degrees; use robust spiral or ring side binding.
- Link tabs logically to the index and make them large enough to select reliably.
- Reserve margin space for binding and a thumb used as a cursor.
- Use clear sans-serif text; approximately 12 pt body and 14 pt headings, with respective minima of 10 and 12 pt, assessed at about 600 mm.
- Keeping a drill on one page can justify using the stated minimum rather than preferred type size.

This is human-factors guidance with a broader operational context, not a mandatory private-C172 page template.

The 1991 [FAA-sponsored study, Appendix A, printed page A-2](https://www.faa.gov/sites/faa.gov/files/2022-11/VNTSC%20Rpt%20DTO-VNTSC-FAA-91-7.pdf), favors limiting a normal card checklist to one Letter sheet, laminated or trifold, because of clipping, stowing, retrieval, and repeated page turning. That recommendation concerns a normal card's usability; it is not a requirement to squeeze every emergency, preflight detail, and explanation onto the same sheet. It provides a useful counterweight to simply adding pages indefinitely.

## Candidate formats for our document

The following are design proposals inferred from the references, not claims that our content already fits them.

| Candidate | Proposed construction | Main benefit | Main cost or unanswered question |
|---|---|---|---|
| Folded Letter sheet | Two 5.5 × 8.5 in panels per face; four panel faces after folding | Closest to the original two-sided sheet; easy home printing | Finite area; folding provides access, not extra capacity. Current content at 12 pt needs a fit study. |
| Larger reference cards | 6.5 × 9 in, normal and emergency separated as needed | More width for challenge/response pairs than narrow columns | Less efficient Letter printing; finished size must fit the intended holder. |
| Small card set | 5 × 8 in, individually identified and possibly ring-bound | Portable; cards can group related phases | More faces and retrieval decisions; narrow lines can wrap heavily. |
| Half-Letter flipbook | 5.5 × 8.5 in portrait, initially one content column per page | Straightforward Letter printing; room for readable text without a fixed total-page constraint | More page turns; binding, tabs, and thumb margins consume space. |
| Short normal card plus reference book | Frequently used checks on a card; fuller procedures in a small indexed book | Separates routine scanning from detailed lookup | Requires deliberate content classification and clear cross-references during content QA. |
| Full Letter pages | Continue the current 12 pt portrait experiment | Already rendered; useful readability baseline | Handling and cockpit storage need evaluation; page count alone says little about usability. |

A Letter trifold is also historically established, but narrower fold panels are unlikely to improve our long challenge/response rows. I would rank it below the half-fold or small book for this particular content. That is a layout inference, not a measured fit result.

## Recommended reference basis and next experiment

Use **CAP 676 for evaluation criteria**, **Diamond for a multipage document example**, **Qref for small card/book construction**, and **Oklahoma for half-sheet organization and printing**. CheckMate supplies a useful larger-card size comparator. No single example needs to supply every design choice.

My first candidate would be a **5.5 × 8.5 in portrait flipbook with one content column**, 12 pt body and 14 pt headings. Half-Letter is a practical adaptation to our printer target, not a universal aviation standard. Our current portrait Letter version uses two 4 in-wide columns; a single column on a half-Letter page can be wider even after allowing a binding margin, but the page is shorter. That exchanges some wrapping for more page boundaries. The resulting page count must be measured.

For a meaningful comparison, render the same content in a **6.5 × 9 in card format** too. Compare complete-procedure placement, wrapping, face count, and navigation at actual size. Keep the existing Letter PDFs as baselines. Do not shorten procedures merely to make the comparison fit.

After that comparison, content QA can determine whether a short normal card plus fuller reference book would be useful. In particular, resolving the remaining engine-out duplication and deciding which explanations belong in a reference document are content decisions, not spacing adjustments.

Printing should preserve the composed page size. Two-up output should arrange the smaller pages on Letter sheets without reducing them; a folded booklet also needs the correct page order and duplex orientation. A ring-bound stack and a folded booklet require different print arrangements even if their finished pages have identical dimensions.

This research adds a reference basis only. It does not change the renderer, checklist wording, or comparison PDFs.

Subsequent implementation: see [the physical-format comparison](text-size-study.md#physical-format-comparison) for rendered half-Letter, reference-card, Legal, and Tabloid alternatives after relaxing the Letter-only printing constraint.
