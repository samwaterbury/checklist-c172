# POH comparison: notes, conditions, and candidate changes

Historical audit of checklist commit `02a1d94`, reviewed 2026-09-12. The findings below preserve that audit baseline. Current decisions and later changes are tracked only in [Content decisions](content-decisions.md).

The proposed blanket conversion of instructional notes into action blocks does **not** survive the POH check. The supplied manual explicitly uses NOTE blocks and attached parentheticals for many of these instructions. Those treatments should remain. Two narrowly supported presentation changes survive; several more consequential content discrepancies also need review.

## Reference and scope

Source: [C172S-G1000-POH.pdf](/Users/sam/Downloads/C172S-G1000-POH.pdf), 352 PDF pages. Its introduction identifies it as an **Information Manual**, reproducing the POH/AFM at original issue, **20 December 2007**, part **172SPHBUS-00** (Information Manual part **172SIMBUS-00**), for **172S NAV III / GFC 700 AFCS**. The cover lists serials 172S10468, 172S10507, 172S10640, and 172S10656 onward. The notice states that the Information Manual is not kept current. These details appear on PDF pages 1 and 5, printed i and v/vi.

Accordingly, “POH alignment” below means alignment with **this supplied edition**. Its applicability to the particular aircraft and its current POH/supplements remains to be confirmed before adopting operational changes. The source notice is evidence about the document, not an instruction to alter the user's requested workflow.

Source SHA-256: `11bb6be70757984fc7b05a69bc8242bdcbc79cf73604c5837364bd8013aa9b0a`.

Three parallel reviews covered emergency procedures, preflight/starting, and other normal procedures. We inventoried **all 48 existing note-bearing rows, qualifiers, and conditional/nested groups** in the current 25-procedure layout. The removed shorter engine-out duplicate was excluded. We searched the full extracted PDF, checked relevant expanded procedures and system descriptions, and visually inspected the source checklist pages to distinguish numbered actions, parentheses, NOTE blocks, WARNING blocks, and conditional headings. Major numerical and emergency-branch findings were independently rechecked during synthesis.

This is a complete inventory of that focused candidate set, **not a complete verification of every procedure, omission, or aircraft configuration**. Nearby discrepancies found during the review are recorded separately rather than silently expanding the checklist.

Page references use **printed page first, then the one-based PDF page**, e.g. `3-7 / PDF 73`.

## How the filter was applied

- **Keep:** the existing instruction, condition, and its role/attachment correspond to the source. Different line wrapping, point size, capitalization, or compact layout alone is not a reason to redesign it.
- **Presentation candidate:** a concrete difference in the source's action/condition structure supports a limited change. No new operating instruction is introduced.
- **Content candidate:** a value, action, condition, or required scope differs from the source. Correcting it is a separate content decision; changing the visual component alone is insufficient.
- **Not located / uncertain:** the particular reminder was not found, or its local use is unclear. This does not establish that the underlying subject is absent from the POH, nor that an edit is automatically appropriate.

Keep and candidate can apply to different aspects of one row: for example, keep a battery-test parenthetical while correcting its duration.

## Two presentation candidates that survive

| Candidate | Current checklist | Source comparison | Narrow proposal |
|---|---|---|---|
| **P1. Flap-dependent emergency airspeeds** — `engine-out-after-takeoff-airspeed`, `ln-airspeed` | A single `65–70 KIAS` response, with the flap-to-speed mapping in an italic note. | The source gives two explicit action response lines: **70 KIAS — flaps UP** and **65 KIAS — flaps 10°–FULL**. 3-6 / PDF 72; 3-8 / PDF 74. | Use the two source-specific responses directly. Preserve both speeds and their conditions; remove the locally introduced undifferentiated range. |
| **P2. Priming completion criterion** — `prime-rich` | `Full Rich`, followed by a parenthetical note combining approximate 3–5 seconds and stable flow. | In source step 13, **until stable fuel flow is indicated** belongs to the main action; **approximately 3 to 5 seconds** is parenthetical. 4-12 / PDF 118. | Put the stable-flow endpoint with the action; retain the approximate timing as supporting parenthetical text and the following cutoff step. Do not turn priming into a fixed-duration instruction. |

**Deferred under the strict filter:** moving “continue cranking” in `fs-magnetos` or “prior to touchdown” in the two landing-door rows into larger action text. The source gives those words action-level prominence, but their meaning and attachment already survive in our checklist. These are weaker typography choices, not changes needed for this pass.

The priming box itself need not be removed to resemble the POH. The source groups the same pump/mixture/pump actions; its missing warm-engine NOTE is a separate content candidate below.

## Content candidates found while checking the notes and conditions

These are source discrepancies to review, not an approved replacement flight procedure. Preserve any already-matching note/parenthetical treatment while addressing the specific mismatch.

| Candidate | Current versus supplied source | Source | Proposed review |
|---|---|---|---|
| **C1. Electrical-fire recovery** — `el-extinguished`, `el-air-off-again`, `el-power-needed` and children | The post-extinguishment CABIN HT/AIR response is **OFF** locally but **ON** in the source, subject to complete extinguishment. The next branch contains battery/voltage checks that appear in **Starting Engine**, instead of the source's circuit-breaker and electrical-restoration steps. The condition also omits continued flight to the nearest suitable airport/landing area, and the explicit ventilation WARNING is absent. | 3-11–3-12 / PDF 77–78; misplaced checks compare with 4-12 / PDF 118. | **Review the whole recovery branch first**, including warning placement, condition scope, actions, and order. Do not treat the misplaced checks as POH-uncovered personal additions or fix only their styling. |
| **C2. Standby-battery test** — `se-battery-test` | **10 seconds / verify green lamp** locally; **20 seconds / verify green TEST lamp does not go off** in source. | 4-12–4-13 / PDF 118–119. | Reconcile duration and continuous-lamp criterion with the applicable aircraft source. Keep the parenthetical verification format. |
| **C3. Magneto drop limit** — `run-up-magnetos` | **175 RPM** locally; **150 RPM** in source. The **50 RPM differential** matches. | 4-16 / PDF 122; independently repeated in 4-29 / PDF 135. | Correct the differing limit after applicability review; retain the parenthetical criterion and matching differential. |
| **C4. Main-bus threshold** — `se-bus-m` | **Less than 1.5 V** locally; **1.5 V or less** in source. | 4-12 / PDF 118. | Restore the inclusive boundary; retain qualifier treatment. The similar electrical-fire row is handled through C1, not independently legitimized. |
| **C5. Warm-engine priming condition** — `se-priming` | No warm-engine exception above the box. Source places a **NOTE** immediately before priming to omit those steps when the engine is warm. | 4-12 / PDF 118; expanded starting discussion 4-25 / PDF 131. | Restore that source NOTE and its scope. Do not invent a “cold engine only” rule or relabel the source NOTE as a branch. |
| **C6. Mixture after engine start** — `se-mixture-rich` | “Advance smoothly” is present, but **when engine starts** is missing. | 4-12 / PDF 118, step 16. | Restore the source timing condition attached to its action. |
| **C7. In-flight restart conditions and note content** — `eo-mixture`, `eo-magnetos` | Mixture lacks **if restart has not occurred**; MAGNETOS action lacks its inline **START if propeller is stopped** alternative. The first NOTE is shortened and omits the source's mixture adjustment to obtain smooth operation. | 3-7 / PDF 73. | Restore missing conditions and operational note content **in their source roles**. Keep the NOTE as a NOTE, rather than converting its whole paragraph into a new branch. |
| **C8. Landing MASTER timing** — `ln-master`, `landing-with-power-master-switch-alt-bat` | Both omit the source condition **when landing is assured**. | 3-8 / PDF 74, both landing procedures. | Restore the condition on the affected action. This is separate from the already-present door timing. |
| **C9. Takeoff flap response** — `before-takeoff-wing-flaps` | **Up (10° preferred)** locally; **UP–10° (10° preferred)** in source. | 4-17–4-18 / PDF 123–124. | Restore the source range while preserving the already-matching preference. |
| **C10. Ground-leaning scope** — `se-lean`, `run-up-mixture-control-2` | Generic “as necessary” abbreviates an expanded ground-operation procedure. The source also has a NOTE specifically covering further ground operation after Before Takeoff. | 4-26 / PDF 132; 4-38 / PDF 144. | Review the shared ground-leaning scope and reference/criteria. It is covered by the source, not automatically a personal addition; do not use a formatting change to invent a procedure. |
| **C11. Descent/approach mixture criterion** — `approach-mixture-control` | **If necessary** locally; **if necessary to make engine run smoothly** in source Descent. | 4-20 / PDF 126. | Restore the fuller criterion within the existing qualifier. |

The source also includes **RPM** after the cruise power range; adding that missing unit is a small content-alignment candidate. The cruise power note itself already matches and should stay unchanged (4-19 / PDF 125).

## Earlier suggestions filtered out: keep these treatments

| Item | Why it should stay |
|---|---|
| Both in-flight engine-out notes | Both are explicitly labeled **NOTE** in the source (3-7 / PDF 73). C7 addresses omitted content, not conversion into conditional action blocks. The immediate-zero-flow note already preserves its relevant condition and action. |
| Fire-not-extinguished airspeed continuation | The source attaches it parenthetically to the airspeed step, not as a separate branch (3-11 / PDF 77). Keep that relationship. |
| “If Engine Starts” / “If Engine Fails to Start” | Source has these same alternative headings and branch boundaries (3-10 / PDF 76). No generic redesign or newly inferred memory-item meaning for boxes. |
| Takeoff/climb mixture notes above 3000 ft | Corresponding parentheticals appear in normal takeoff and enroute climb (4-18–4-19 / PDF 124–125). |
| Cruise 75% power note | Corresponding parenthetical appears in Cruise (4-19 / PDF 125). |
| Pitot heat within 30 seconds | Source uses a parenthetical verification with the action (4-6 / PDF 112); general preflight discussion also covers it. |
| Minimum five-quart oil note | Source presents the minimum as an explicit **NOTE** (4-8 / PDF 114). |
| Matching verification/selection qualifiers | No-red-X criteria, minimum 24 V, LOW VOLTS not shown, “FULL recommended,” “on final,” magnetos exception, and best-glide descriptor have source support. See the full inventory for references. |
| Forced-landing cross-reference and ditching radio parenthetical | Their attachment and purpose match source steps (3-11 / PDF 77; 3-9 / PDF 75). This does not establish completeness of the surrounding procedures. |

## Items potentially outside the source

No whole operational candidate in this review was established to be wholly uncovered by the supplied manual.

- The exact **ASI/AI/TC/BARO/VSI/DG** mnemonic was not located. The underlying instrument checks are covered. It is explanatory, so no change is recommended.
- The generic **adjust map settings** reminder was not located as a POH checklist requirement. This is the only plausible optional personal-action formatting candidate: if retained as a personal task, it could be a normal action. **Hold it out of the selected changes for now.** The attached **set heading bug** instruction is covered elsewhere in context-specific navigation/autopilot guidance (4-17 / PDF 123 and 4-20 / PDF 126), so the combined note must not be called “not covered.”
- Ground leaning, landing-light use, and alternator-belt inspection are discussed elsewhere in the manual even where they do not appear in the corresponding concise checklist. Their placement does not establish absence from the POH.

## Additional findings to queue for full content QA

These were encountered while checking nearby source context. They are not part of the two presentation proposals and are not an exhaustive omission list.

| Area | Discrepancy to review | Printed / PDF reference |
|---|---|---|
| Electrical-fire recovery | C1 above is a substantive procedure mismatch, not an isolated wording issue. | 3-11–12 / 77–78 |
| Engine fire during start | Missing “for a few minutes” at 1800 RPM, continue-cranking instruction in failed-start branch, and repair/replace-before-further-flight scope. Existing branch headings still match. | 3-10 / 76 |
| Other emergency completeness | Ditching ends substantially earlier than the source and narrows its flap setting; takeoff/after-takeoff engine-out and powered landing also omit source steps. Audit complete procedures before describing them as POH-complete. | 3-6, 3-8–9 / 72, 74–75 |
| Battery/engine-start verification | ARM/PFD-on criterion, STBY BATT annunciator shown, starter-release condition, and oil-pressure rise/time criteria are absent or abbreviated. | 4-12–13 / 118–119; expanded 4-25 / 131 |
| Starting sequence | Source clears propeller area before MASTER ON and priming; local clearance appears later. Flooded-start NOTE is also absent. | 4-12 / 118 |
| Preflight avionics fans | Local “Verify Fans” compresses the separate BUS 1/BUS 2 on/check/off sequence, including explicit return to OFF. | 4-5–6 / 111–112 |
| Preflight checks | Alternate static valve CHECK versus source OFF; abbreviated extinguisher and PFD criteria; missing empennage control-surfaces check; fuel-sampling instructions/contamination warning shortened to CHECK. | 4-5–10 / 111–116 |
| Autopilot verification | Source includes overpower checks and disconnect/aural-alert verification absent from local After Start sequence. | 4-15–16 / 121–122 |
| Shutdown | Local throttle 1000 RPM versus source IDLE; source parking-brake step also absent. | 4-22 / 128 |
| Normal flap retraction | Source includes context-dependent retraction conditions; local After Takeoff UP lacks one. Confirm which takeoff procedure the combined section represents. | 4-18 / 124 |

## Recommended next step

Resolve **C1–C3** against the applicable aircraft/revision first: electrical-fire recovery, standby-battery testing, and the magneto limit. The original **presentation-only** shortlist was **P1 and P2**. The user retained P1 and chose to revert P2 after previewing it. Keep the POH's existing note and parenthetical roles elsewhere. P1, the replacement of C1’s copied restoration rows, C3/C4/C9, and the cruise RPM unit are implemented. C2 and C5–C8 were reviewed and intentionally retained as-is. The other C1 issues and C10–C11 remain review candidates. P2 was reverted and is not an active change.

## Full 48-entry audit trail

The tables below preserve the per-item evidence behind the shortlist. “Keep” concerns the scoped treatment, not a certification of every neighboring instruction. For fire-start cranking and landing-door timing, the final conservative disposition is **DEFER** despite their source typography differences.

### Emergency procedures — 22 entries

| ID | Source location | Source treatment / comparison | Disposition and narrow action |
|---|---|---|---|
| `eo-airspeed` | 3-7 / PDF73, step1 | 68 KIAS with parenthetical “best glide speed.” | KEEP existing qualifier. |
| `eo-magnetos` | 3-7 / PDF73, step6 + first NOTE | The stopped-propeller discussion is expressly labeled NOTE. Source step6 separately includes the START alternative. Source NOTE additionally covers windmilling restart and leaning mixture to smooth operation; current note stops after advancing throttle. | KEEP note role; reject converting entire note into new conditional heading. POH-ALIGNMENT CANDIDATE for restoring the missing step6 alternative and omitted operational portion of NOTE, keeping original role and scope. |
| `eo-pump-off` | 3-7 / PDF73, step7 + second NOTE | Immediate-zero-flow condition and return-pump-ON action are expressly a NOTE. Current note retains those condition/action words, abbreviating diagnostic explanation and display label. | KEEP; strongest exclusion from earlier generic recommendations. No new branch needed. |
| `ln-airspeed` | 3-8 / PDF74, no-power landing step3 | Source has two equal-level action response lines: 70 KIAS—Flaps UP; 65 KIAS—Flaps10°–FULL. Current 65–70 KIAS range moves selection criteria into small italic note. | POH-ALIGNMENT CANDIDATE: use the source's two flap-specific action responses, without changing speeds. |
| `ln-flaps` | 3-8 / PDF74, step7 | AS REQUIRED (FULL recommended). | KEEP existing qualifier. |
| `ln-doors` | 3-8 / PDF74, step10 | UNLATCH PRIOR TO TOUCHDOWN is the main action response, without parentheses. Current timing is a small parenthetical qualifier placed before UNLATCH. | DEFER presentation change: source places timing in main response, but current qualifier preserves the instruction and timing. Do not select under the strict filter. |
| `ef-airspeed` | 3-11 / PDF77, engine-fire step7 | Source places if-fire-not-extinguished condition inside a parenthetical continuation of the 100-KIAS step, not a new branch and not a labeled NOTE. Current note is also attached parenthetically to this step and paraphrases the action/limit. | KEEP attachment/condition and avoid inventing branch. Optional typography-only alignment would render this as action continuation rather than generic note, but source-compatible parenthesis alone does not compel a change under user's conservative rule. |
| `ef-landing` | 3-11 / PDF77, engine-fire step8 | EXECUTE with parenthetical cross-reference to emergency landing without engine power. Current pointer names our corresponding title. | KEEP secondary cross-reference and matching destination. |
| `fs-magnetos` | 3-10 / PDF76, step1 | START (continue cranking to start the engine) is the complete bold immediate-action step. Current continuation is a small light italic note. | DEFER presentation change: current wording and attachment preserve the source instruction. Source bold emphasis is a typography difference; do not select under the strict filter. |
| `fs-starts` | 3-10 / PDF76 | IF ENGINE STARTS heading governs power and shutdown/inspection steps. | KEEP branch boundaries and condition; box is local layout decoration. See missing power-duration qualifier below. |
| `fs-inspect` | 3-10 / PDF76, engine-starts step3 | Engine—SHUTDOWN (inspect for damage). | KEEP as attached parenthetical instruction, not standalone condition. Source puts qualifier after action; user rule does not justify a global cosmetic reorder. |
| `fs-fails` | 3-10 / PDF76 | IF ENGINE FAILS TO START heading governs the ensuing 14 steps. | KEEP branch boundary/condition. Some omitted continuations are separately noted below. |
| `el-switches` | 3-11 / PDF77, electrical-fire step7 | All Other Switches (except MAGNETOS switch)—OFF. | KEEP exception attached to switch selection. |
| `el-extinguished` | 3-11 / PDF77, WARNING then steps8–9 | No source heading with precisely these words. Source gives explicit WARNING before ventilation and repeats “when sure that fire is completely extinguished” on each of steps8–9. Local shared condition governs the right two steps but loses sure/completely specificity and warning identity; second response is wrong. | POH-ALIGNMENT CANDIDATE: reconcile warning/condition wording and represent source warning before ventilation. Do not simply re-style existing heading as sufficient. Response mismatch below is substantive. |
| `el-power-needed` | 3-12 / PDF78 | Official conditional heading includes “FOR CONTINUED FLIGHT TO NEAREST SUITABLE AIRPORT OR LANDING AREA”; current truncates that scope. Official children are circuit-breaker and power-restoration steps; current children are start-system diagnostic checks. | POH-ALIGNMENT CANDIDATE: restore source condition scope and reconcile children as a unit. Retain conditional-heading role. This is highest priority. |
| `el-bus-e` | Current electrical-fire branch; source 4-12 / PDF118 step5 (also external-power start 4-13 / PDF119 step5) | Verify24-V-minimum instruction exists under STARTING ENGINE, not source electrical-fire restoration. | POH-ALIGNMENT CANDIDATE as misplaced child of `el-power-needed`; do not bless it as an unsupported/custom emergency addition. |
| `el-bus-m` | Current electrical-fire branch; source 4-12 / PDF118 step6 (also 4-13 / PDF119 step6) | Verify1.5-V-or-less instruction exists under STARTING ENGINE, not electrical-fire restoration. Current less-than differs from source “or less,” but relocating/replacing this whole emergency branch takes priority. | POH-ALIGNMENT CANDIDATE as misplaced child; no independent typography fix. |
| `engine-out-after-takeoff-airspeed` | 3-6 / PDF72, after-takeoff step1 | Source uses two explicit flap-dependent airspeed response lines, both bold immediate-action text. Current range + small note hides that distinction. | POH-ALIGNMENT CANDIDATE as for `ln-airspeed`: promote both exact flap-dependent responses. |
| `engine-out-after-takeoff-wing-flaps` | 3-6 / PDF72, after-takeoff step5 | AS REQUIRED (FULL recommended). | KEEP qualifier. |
| `ditching-radio` | 3-9 / PDF75, step1 | Source action is TRANSMIT MAYDAY on121.5MHz with parenthetical location/intentions/squawk7700 continuation; no labeled NOTE. | KEEP semantic attachment and wording. As with `ef-airspeed`, optional same-size action continuation better reproduces source hierarchy, but do not introduce an independent procedure or conditional branch merely because the continuation contains verbs. |
| `landing-with-power-wing-flaps-2` | 3-8 / PDF74, powered landing step6 | FULL (on final approach). Current “On final” equivalent attached qualifier. | KEEP. |
| `landing-with-power-doors` | 3-8 / PDF74, powered landing step10 | UNLATCH PRIOR TO TOUCHDOWN main action, without parentheses. | DEFER presentation change, matching `ln-doors`: timing and instruction already survive in the qualifier. |


### Starting and preflight — 13 entries

| Checklist ID | Disposition | POH comparison and narrow recommendation |
|---|---|---|
| `se-battery-test` | **POH-ALIGNMENT CANDIDATE (content)** | Checklist says hold TEST for **10 seconds**, verify green lamp. POH 4-12/PDF118 item3a says **20 seconds** and verify green TEST lamp **does not go off**. Same instruction appears at 4-13/PDF119 for external power. Correct duration and continuous-lamp criterion to supplied source; keep them attached as parenthetical verification, rather than inventing a separate branch. POH itself uses parentheses. Section7-52/PDF254 refers back to Section4; it supplies no alternative10-second test. |
| `se-indicating` | **KEEP** | No-red-X verification is parenthetical in POH4-12/PDF118 item4; existing qualifier is a faithful abbreviated criterion. Do not promote purely on generic typography grounds. |
| `se-bus-e` | **KEEP** | Minimum24V matches parenthetical verification in POH4-12/PDF118 item5. |
| `se-bus-m` | **POH-ALIGNMENT CANDIDATE (content)** | Current “Less than1.5 volts” excludes exactly1.5V; POH4-12/PDF118 item6 says **1.5 VOLTS or less**. Correct inequality; retain qualifier role. This is a narrow wording discrepancy, not grounds to redesign all qualifiers. |
| `se-priming` | **POH-ALIGNMENT CANDIDATE (missing condition)** | Box accurately groups pumpON, rich/cutoff, pumpOFF. POH4-12/PDF118 inserts explicit **NOTE** before these steps: omit priming steps12–14 if engine is warm. Current box has no warm-engine omission. Add equivalent note before/at box, with scope to complete box; preserve POH note treatment, do not invent a new action/branch label. Amplified4-25/PDF131 contains nuanced hot-start behavior, so do not substitute an unqualified invented “cold engine only” heading. No need to remove box or combine mixture rows solely to copy POH typography. |
| `prime-rich` | **POH-ALIGNMENT CANDIDATE (action/criterion distinction)** | POH4-12/PDF118 item13 makes **until stable fuel flow is indicated** part of the main mixture action; only approximate3–5seconds is parenthetical. Current note puts both timing and stable-flow endpoint in secondary italic parentheses. Narrow candidate: associate “until stable fuel flow” directly with the FULL RICH action, leave approximate timing parenthetical, followed by existing IDLE CUTOFF row. Preserve stable flow as endpoint rather than implying a fixed timed prime. This is a real source distinction, unlike ordinary parenthetical notes. |
| `se-mixture-rich` | **POH-ALIGNMENT CANDIDATE (missing condition/action wording)** | POH4-12/PDF118 item16 is “ADVANCE SMOOTHLY TO RICH (when engine starts).” Checklist puts advance-smoothly in a qualifier and omits when-engine-starts. Narrow candidate: restore timing condition and source action wording, still attached to mixture row; do not add standalone decision heading. |
| `se-low-volts` | **KEEP** | Not-shown verification is explicitly parenthetical in4-13/PDF119 item19. |
| `se-nav` | **KEEP** | “ON as required” is POH4-13/PDF119 item20. Moving “as required” into checklist qualifier preserves meaning. No redesign justified solely because source has no parentheses here. |
| `se-lean` | **POH-ALIGNMENT CANDIDATE, defer to content QA** | Not an uncovered school-only addition: amplified4-26/PDF132 prescribes ground leaning after start when engine runs smoothly, with three steps (1200RPM, lean for maximumRPM, throttle to ground-operation RPM, recommended800–1000). Current “Lean (As necessary)” is vague and misses scope/criterion. Review against complete amplified procedure, not a formatting-only promotion of “as necessary.” |
| `preflight-cabin-low-fuel-annunciators` | **KEEP** | Not-shown criterion matches parenthetical in4-5/PDF111 item12. |
| `preflight-cabin-pitot-heat-switch` | **KEEP** | POH4-6/PDF112 item21 explicitly puts warm-to-touch within30sec in parentheses following ON. POH4-4/PDF110 general preflight NOTE also contains that requirement. Current attached italic note has corresponding role and condition; **do not promote it simply because it instructs a check**. Section7-64/PDF266 describes system but changes no timing. Current omits “carefully/to the touch”; this is not evidence the entire note should become a branch. |
| `preflight-nose-oil-level` | **KEEP** | POH4-8/PDF114 oil dipstick/filler item2 is followed by a literal **NOTE** containing minimum5quarts and fill8quarts for extendedflight. Existing5quart restriction belongs in a note under user's source-preservation rule. Section8-14/PDF296 repeats5quart minimum. Separate omission of extendedflight fill guidance may be considered in full content QA; do not turn existing note into an action to satisfy generic design advice. |


### Other normal procedures — 13 entries

| Current item ID | Current detail | Decision | POH evidence / narrow disposition |
|---|---|---|---|
| `as-instruments` | Flight Instruments—Check; `(ASI/AI/TC/BARO/VSI/DG)` | NOT-LOCATED (mnemonic only); no change recommended | 4-15/PDF121 Before Takeoff has Flight Instruments (PFD)—CHECK (no red X's), and separate Standby Flight Instruments check. This exact six-instrument mnemonic was not located in the supplied PDF; it is explanatory indexing, not a hidden action. Do not claim instrument checks themselves are uncovered. |
| `run-up-flight-instruments` | `(No red Xs)` | KEEP | 4-15/PDF121 step 6 attaches this same criterion parenthetically to Flight Instruments (PFD)—CHECK. |
| `run-up-magnetos` | `(RPM drop should not exceed 175 RPM on either magneto or 50 RPM differential between magnetos)` | POH-ALIGNMENT CANDIDATE: numerical correction | 4-16/PDF122 step 18a says **150 RPM**, not 175; 50 differential matches. Expanded Magneto Check 4-29/PDF135 independently repeats 150 and 50. Restore 150; retain attached parenthetical criterion rather than promoting it solely for design reasons. High confidence. |
| `run-up-fms-gps-flight-plan` | FMS/GPS Flight Plan—As Desired; `(Adjust map settings and set heading bug)` | MIXED: map reminder NOT-LOCATED; heading instruction COVERED ELSEWHERE, placement UNCERTAIN | 4-16/PDF122 step 25 is FMS/GPS Flight Plan—AS DESIRED, followed by a distinct NOTE to check GPS availability on AUX-GPS STATUS; current map/heading note is not that POH note. The exact generic map-settings action was not located in supplied PDF. Heading-bug operation **is** covered: 4-17/PDF123 and 4-20/PDF126 give a WARNING concerning manual navigation-source change with AP engaged, ROL reversion, then setting HDG bug and correct nav source before engaging another mode. Therefore only map-settings reminder is a potential custom action candidate; do not label the whole note uncovered or transpose the context-specific warning into a generic action. Current `before-takeoff-hdg-sel` also already exists. |
| `run-up-mixture-control-2` | Mixture Control—Lean `(As necessary)` | POH-ALIGNMENT CANDIDATE: restore condition; format need not change | Expanded 4-26/PDF132 explicitly says, in a NOTE, **if further ground operation is required after BEFORE TAKEOFF**, lean again as described until ready for TAKEOFF. That procedure sets 1200 RPM, leans for maximum RPM, then sets appropriate ground RPM (800–1000 recommended). Generic "As necessary" loses the source's ground-operation condition. A scoped qualifier/reference to ground leaning can improve alignment; no reason to remove NOTE status merely because it includes instructions. Section 4-38/PDF144 reinforces the procedure. |
| `before-takeoff-wing-flaps` | Wing Flaps—Up `(10° preferred)` | POH-ALIGNMENT CANDIDATE: restore range | 4-17/PDF123 step 29 and 4-18/PDF124 Normal Takeoff step 1 both say **UP–10° (10° preferred)**. Current single "Up" response drops the allowed range and conflicts visually with the preferred value. Restore UP–10°; keep the matching preference parenthetical. |
| `before-takeoff-mixture-control` | RICH; `(Above 3000 feet pressure altitude, lean for maximum RPM)` | KEEP | 4-18/PDF124 Normal Takeoff step 3 and Short Field Takeoff step 4 use this same attached parenthetical. It is not a separate decision heading in POH. Expanded 4-30/PDF136 adds full-throttle/stationary setup, but this doesn't justify changing the already matching checklist parenthetical in this pass. |
| `after-takeoff-mixture-control` | Same 3000-ft note | KEEP | 4-19/PDF125 Enroute Climb step 3 uses the same attached parenthetical. |
| `cruise-power` | Power—2100–2700; `(No more than 75% power recommended)` | KEEP note; optional separate POH-ALIGNMENT correction to response unit | 4-19/PDF125 Cruise step 1 has **2100–2700 RPM**, with the exact same parenthetical. Preserve the condition as-is. Adding the missing RPM unit aligns the response but is not an action/note redesign. |
| `cruise-land-light-switch` | LAND Light Switch—OFF `(If applicable)` | KEEP for this pass | No equivalent row in concise Cruise list 4-19/PDF125, but expanded Landing Lights 4-30/PDF136 recommends only taxi light to enhance visibility enroute/in traffic pattern. Thus this is not an uncovered topic. No hidden action or contrary criterion identified. |
| `cruise-mixture-control` | Mixture Control—Lean `(As necessary)` | KEEP for this pass | 4-19/PDF125 has LEAN `(for desired performance or economy)`. Current phrasing is an abbreviated generic cue, not grounds for new branch styling. If later pursuing wording fidelity, source purpose can replace generic qualifier, but no material lost condition was established here. Expanded leaning discussion 4-35–38/PDF141–144 means this topic is firmly covered by POH. |
| `approach-mixture-control` | Mixture Control—Adjust `(If necessary)` | POH-ALIGNMENT CANDIDATE: restore criterion | 4-20/PDF126 Descent step 2 has ADJUST **(if necessary to make engine run smoothly)**. Current qualifier truncates the condition's purpose. Restoring that criterion improves alignment; retain an attached qualifier, not a separate branch. |
| `after-landing-mixture-control` | Mixture Control—Lean `(As necessary)` | KEEP presentation; procedure scope clarification possible in broader QA | Concise After Landing 4-22/PDF128 only lists Wing Flaps UP, but expanded 4-26/PDF132 explicitly covers **all ground operations** once engine is running smoothly. Do not classify postlanding ground leaning as not covered. As with run-up, if adding a shared ground-leaning procedure, point to 1200 RPM / max RPM / ground RPM rather than invent a new sequence. |

