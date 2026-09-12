# Emergency procedures: coverage, placement, and outstanding POH content

Reviewed 2026-09-13 against the current working-tree checklist, after the Ditching and takeoff engine-failure additions. This is a new, broader emergency review; the earlier 48-item note/condition audit was not a full Section 3 inventory.

**Historical audit:** This report preserves the working-tree baseline reviewed on 2026-09-13, before Cabin Fire and Wing Fire were added and before subsequent landing and fire simplifications. References to “current” below mean that audit baseline. See [Content decisions](content-decisions.md) for the current status.

## Scope and interpretation

Source: [supplied C172S G1000 Information Manual](/Users/sam/Downloads/C172S-G1000-POH.pdf), original issue 20 December 2007, 172SPHBUS-00 / 172SIMBUS-00, NAV III / GFC 700. References below are **printed page / one-based PDF page**. Section 3 runs from PDF 67 through 106, including contents and blank leaves; its concise procedures are 3-6 through 3-24, and amplified material is 3-25 through 3-39/3-40. Optional-equipment emergency procedures require the applicable Section 9 supplement; the supplied supplement material is separately cataloged below. This reviews this supplied edition, not a different aircraft's current POH or absent supplements.

Checklist baseline: the procedure content and emergency placement at the audit date. Its nine represented concise procedure families and their omissions are preserved below. The current [content](../content/procedures.yaml) and [layout](../layout/kneeboard.yaml) have since changed; they are not frozen copies of the audit baseline.

No checklist content, typography, placement, or PDF was changed during this review. Prior decisions remain decisions: C7 restart wording and C8 MASTER timing were explicitly retained earlier; C1's warning/condition/ventilation response were left unchanged under the user's narrower authorization. They still appear here because the current request asks for all outstanding differences. Inclusion in this catalog is not approval to change them. Previously discussed start-fire and powered-landing omissions are distinguished from newly found whole procedures.

This is a semantic catalog of missing actions, conditions, notes, warnings, and explanatory material, not a list of every capitalization, punctuation, abbreviation, or line-break difference. Terms such as FPM versus FT/MIN, '&' versus 'and', and removal of 'Switch' or 'Control Knobs' from otherwise recognizable labels are not automatically new instructions. Numbered-step presence is distinguished from complete preservation of its wording.

## Findings at a glance

- The current cards represent **9 of 27 concise Section 3 procedure families**. **18 whole families are absent**. This counts the CO persistent-alert branch as part of its parent procedure and counts the four red-X instrument cases separately. Amplified-only procedures and Section 9 equipment procedures are additional, not included in 27.
- All numbered steps now exist in the takeoff-roll, immediately-after-takeoff, no-power landing, start-fire, engine-fire-in-flight, electrical-fire, and Ditching procedures, but some retain missing qualifiers or different responses. In-flight restart retains all seven numbered actions but abbreviates conditions/notes. Powered landing still omits four numbered steps.
- The current grouping is understandable, but powered landing is separated from the other landings. Moving it to the engine-out/landing side provides a clearer division between **engine failure / forced landings** and **fires / systems**.
- The new amplified review finds operational content beyond the earlier shortlist, notably **do not attempt an engine restart after an in-flight engine fire**, forced-landing communication/ELT guidance, and whole procedures for spins, loss of elevator control, and other failures.
- Many paragraphs are training/reference material rather than good candidates for these small cards. The POH itself makes that distinction in its amplified introduction (3-25 / PDF 91). Cataloging them does not imply printing all of them.

## 1. Present procedures and ordering

| Current side and column, top to bottom | Corresponding POH sequence | Assessment |
|---|---|---|
| Engine-out/landing, left: takeoff roll; after takeoff; in-flight restart | Same sequence, 3-6–3-7 / PDF 72–73 | Keep this grouping. It follows flight phase and the POH. |
| Engine-out/landing, right: landing without power; Ditching | POH inserts powered precautionary landing between these, 3-8–3-9 / PDF 74–75 | The two present sections are related; the missing middle member is on the reverse. |
| Fire side, left: engine fire in flight; fire during start | POH lists start fire first, then in-flight engine fire, 3-10–3-11 / PDF 76–77 | Current flight-first order is a reasonable design choice for airborne retrieval. It is not literal POH order. |
| Fire side, right: electrical fire; landing with power | POH places powered landing before Ditching and all fires | This is the least coherent grouping. Powered landing belongs with the other forced-landings procedures. |

**Recommended placement direction (a design judgment, not a POH requirement):**

| Side | Left column | Right column |
|---|---|---|
| Engine failure / forced landings | Takeoff roll → immediately after takeoff → in-flight restart | No-power landing → precautionary landing with power → Ditching |
| Fires / selected systems | In-flight engine fire → start fire; selected additions if space permits | Electrical fire → cabin/wing fire or selected system procedures, depending on content selection |

The exact order of additions on the fire/system side should be chosen after selecting them. Avoid treating an unrelated electrical-power failure as a continuation of electrical fire: its circuit-breaker/reset rules and switch sequence differ. Similarly, cabin fire and electrical fire share steps but are not interchangeable lists. Keep each chosen procedure's conditions and numbered action order intact.

The first proposed move is feasible with the **current wording**: measured at the current 8 pt theme and 174 pt column width, no-power landing + powered landing + Ditching occupy approximately **507.8 pt**, including two 6 pt section gaps, within the 546 pt content region. Existing stretching would fill that nearly-full column. This leaves only about 38 pt of natural spare height there before any further wording restoration. It is a measurement, not a rendered alternate layout or a promise that additional notes will also fit.

Current blank space to the content limit, measured from each column's last baseline:

| Column | Approximate unused height |
|---|---:|
| Engine-out side, left | 224 pt / 3.1 in |
| Engine-out side, right | 156 pt / 2.2 in |
| Fire side, left | 190 pt / 2.6 in |
| Fire side, right | 235 pt / 3.3 in |

These are column-specific vertical spaces, not full-width empty areas. They include no allowance for the new section's heading, line wrapping, or internal spacing. All missing procedures will not fit merely because these totals look large; electrical load-shedding alone carries many actions and conditional notes.

### Titles, retrieval, and emphasis

- **ENGINE OUT - DURING TAKEOFF** omits the POH's **ROLL** qualifier. **AFTER TAKEOFF** omits **IMMEDIATELY**. The actions now match the numbered lists, but the titles are less explicit about when to choose each list.
- **ENGINE OUT - DURING FLIGHT** omits **Restart Procedures**. Adding that distinction would help separate attempted recovery from securing for landing.
- **LANDING - WITH POWER** omits **PRECAUTIONARY**; the source is a precautionary/off-airport procedure, not the normal landing checklist. This matters especially if placed beside other normal-looking landing titles.
- **ENGINE FIRE DURING START** omits **ON GROUND**. The existing title is understandable, but the source's context can be made explicit.
- The source uses selective **bold type for immediate-action/memory items** and states this at 3-6 / PDF 72. The current checklist's uniform medium-weight action text and general bold condition headings do not encode that distinction. Do not describe the current bold styling as a POH memory-item system. Restoring that distinction would be a separate, source-by-source presentation decision, not making every red section or box a memory checklist.
- A cross-reference from engine fire to no-power landing already exists and is useful. If all landings move to the opposite side from fires, retain that explicit link; a simple 'reverse side' cue could be considered without reinstating page numbers.

## 2. Outstanding wording in the nine represented procedures

Classifications below: **action/condition** changes operational content or scope; **explanation** gives rationale or interpretation; **control detail** describes physical travel/direction; **presentation** preserves words but changes their role or placement. The small wording rows are catalog entries, not equal-priority recommendations.

### Engine failure during takeoff roll — 3-6 / PDF 72

All seven numbered steps now appear in POH order.

| Current item | POH material absent or shortened | Type |
|---|---|---|
| `engine-out-takeoff-throttle-control` IDLE | Pull full out. | Control detail |
| `engine-out-takeoff-mixture-control` IDLE CUTOFF | Pull full out. | Control detail |
| Procedure title | During takeoff **roll**. | Scope/title |

MASTER OFF is now present and is no longer an omission. The amplified stop-on-remaining-runway explanation is cataloged separately below.

### Engine failure immediately after takeoff — 3-6 / PDF 72

All nine numbered steps now appear in POH order, including the newly restored door and straight-ahead landing steps.

| Current item | POH material absent or shortened | Type |
|---|---|---|
| `engine-out-after-takeoff-mixture-control` | Pull full out. | Control detail |
| `engine-out-after-takeoff-fuel-shutoff-valve` | Pull full out. | Control detail |
| Procedure title | **Immediately** after takeoff. | Scope/title |

The two airspeeds and flap mappings now match. No reason to restore the old undifferentiated 65–70 KIAS range.

### Engine failure during flight / restart — 3-7 / PDF 73

| Current item | POH material absent or shortened | Type/status |
|---|---|---|
| `eo-shutoff` ON | Push full in. | Control detail |
| `eo-mixture` RICH | **If restart has not occurred.** | Action/condition; previously retained under C7 |
| `eo-magnetos` BOTH | The numbered response itself includes **or START if propeller is stopped**. Current note contains this action, so it is not wholly absent. | Placement/presentation; previously retained under C7 |
| First note at `eo-magnetos` | Windmilling propeller: automatic restart within a few seconds. Stopped propeller can occur at low speeds. | Explanation; previously shortened under C7 |
| Same note | **Lean mixture from full rich as required to obtain smooth operation.** Current note ends at throttle advance. Source says advance throttle **slowly**; current says **smoothly**. | Action plus wording difference; previously retained under C7 |
| Note at `eo-pump-off` | Source identifies **FFLOW GPH** and explains that immediate zero flow indicates engine-driven pump failure. | Instrument label/explanation; the return-pump-ON action and trigger are already preserved |
| Title | Restart Procedures. | Scope/title |

Both source paragraphs are explicitly NOTE blocks. Preserve that role if fuller text is restored rather than turning the whole explanation into a new branch.

### Emergency landing without power — 3-8 / PDF 74

All 12 numbered steps are represented in order.

| Current item | POH material absent or shortened | Type/status |
|---|---|---|
| `ln-mixture` | Pull full out. | Control detail |
| `ln-shutoff` | Pull full out. | Control detail |
| `ln-master` OFF | **When landing is assured.** | Action/condition; previously retained under C8 |
| Seat-back label | Source explicitly identifies pilot and passenger seat backs. | Descriptive scope, implicit in current generic label |

The prior-to-touchdown door qualifier, full-flaps recommendation, flap-dependent airspeeds, touchdown attitude, and braking instruction survive. General forced-landing radio/ELT/electrical timing is in amplified material, not an extra numbered step here.

### Precautionary landing with power — 3-8 / PDF 74

| POH location / current item | POH material absent or shortened | Type/status |
|---|---|---|
| Step 5, between 20° flaps and final-approach FULL | **Selected Field — FLY OVER**, noting terrain and obstructions. | Missing numbered action; previously presented, not implemented |
| Step 7, after FULL flaps | **Airspeed — 65 KIAS** repeated at this point. Current earlier 65 KIAS item remains. | Missing numbered verification, not a missing numeric value |
| `landing-with-power-master-switch-alt-bat` | **When landing assured.** | Action/condition; previously retained under C8 |
| Step 12, after touchdown | **Mixture Control — IDLE CUTOFF (pull full out).** | Missing numbered action; previously presented |
| Step 13, before braking | **MAGNETOS Switch — OFF.** | Missing numbered action; previously presented |
| FULL flap qualifier | Source says 'on final approach'; current says 'on final'. | Equivalent abbreviation, not an extra action |
| Title and seat backs | Precautionary context; pilot/passenger scope. | Scope/title and descriptive wording |

### Ditching — 3-9 / PDF 75

All 13 numbered steps and both NOTE blocks are now represented, including the 20°–FULL response and no-power alternatives.

| Current item | Residual POH wording absent or shortened | Type |
|---|---|---|
| `ditching-heavy-objects` | Objects **in baggage area**; secure or jettison **if possible**. | Scope/condition |
| `ditching-power` 300 FPM @ 55 KIAS | **Establish ... descent**: FPM alone does not explicitly say descent. | More explicit action/direction; value and airspeed preserved |
| Seat-back label | Explicit pilot/passenger scope. | Descriptive wording |
| Notes and face qualifier | Parentheses replace the NOTE labels; folded-coat parenthetical precedes the response locally. | Presentation only; substantive content retained |

Do not mark the already-added approach directions, no-flare-related touchdown attitude, ELT, door evacuation, pressure equalization, or inflation-clear-of-airplane instruction as still missing. The separate amplified statement to **avoid a landing flare** is not itself printed on the card; see below.

### Fire during start on ground — 3-10 / PDF 76

The initial action and both branches contain all source numbered actions in order.

| Current item | POH material absent or shortened | Type/status |
|---|---|---|
| `fs-power` 1800 RPM | **For a few minutes.** | Duration; previously presented |
| `fs-throttle` FULL | Push full in. | Control detail |
| `fs-mixture` IDLE CUTOFF | Pull full out. | Control detail |
| `fs-crank` START | **Continue cranking** in the failed-start branch. Initial top-level action already has its own continue-cranking note. | Action continuation; previously presented |
| `fs-shutoff` OFF | Pull full out. | Control detail |
| `fs-extinguisher` OBTAIN | Have ground attendants obtain it if not installed. | Conditional means/personnel |
| `fs-extinguish` EXTINGUISH | Use fire extinguisher, wool blanket, or dirt. | Means/example alternatives |
| `fs-damage` INSPECT | **Repair or replace damaged components and/or wiring before conducting another flight.** | Follow-on action/condition; previously presented |
| `fs-inspect` SHUTDOWN with preceding 'Inspect for damage' qualifier | Source presents shutdown then inspection in parentheses. Both words survive, but the local qualifier-before-response convention makes the visual reading order less explicit. | Presentation/sequence clarity, not a missing action |
| Title | On ground. | Scope/title |

### Engine fire in flight — 3-11 / PDF 77

All eight numbered actions are represented in order.

| Current item | POH material absent or shortened | Type |
|---|---|---|
| `ef-mixture`, `ef-shutoff` | Pull full out for each. | Control detail |
| `ef-vents` OPEN | **As needed.** | Condition |
| `ef-air` OFF | Push full in; **to avoid drafts**. | Control detail/explanation |
| `ef-airspeed` continuation | Find an airspeed that provides an **incombustible mixture**. Current wording retains increasing glide speed within airspeed limitations to extinguish the fire. | Explanation/endpoint wording, not missing permission to exceed a limit |
| MASTER label | Current label identifies ALT & BAT, matching source scope. | No discrepancy |

The separate amplified **do not attempt to restart the engine** instruction (3-28 / PDF 94) is absent and is an operational addition worth a specific decision. It is not part of the current short airspeed note.

### Electrical fire in flight — 3-11–3-12 / PDF 77–78

| Current item | POH material absent or different | Type/status |
|---|---|---|
| `el-vents-close` CLOSED | To avoid drafts. | Explanation |
| `el-air-off` OFF | Push full in; to avoid drafts. | Control detail/explanation |
| `el-extinguisher` ACTIVATE | **If available.** | Condition |
| Before reopening ventilation | Explicit WARNING: after using the extinguisher, make sure the fire is extinguished before exterior air removes smoke. | Warning absent; earlier user left unchanged |
| `el-extinguished` heading and `el-vents-open` | Source attaches **when sure that fire is completely extinguished** to each ventilation action; local heading says fire has been extinguished. | Condition emphasis/scope is compressed, not wholly absent |
| `el-air-off-again` | **OFF locally versus ON in POH**, with **pull full out** and the complete-extinguishment condition. | Contrary action; earlier left unchanged, not an unresolved extraction ambiguity |
| `el-power-needed` condition | Omits **for continued flight to nearest suitable airport or landing area**. | Destination/purpose condition; earlier left unchanged |
| Restoration steps 10–14 | Circuit breakers CHECK/do not reset, MASTER ON, STBY BATT ARM, BUS 1 ON, BUS 2 ON now match. | Resolved; do not re-flag the deleted battery-test rows |

The current branch heading and generous whitespace help scan the condition, but they do not correct the remaining OFF/ON content difference. That is a separate decision.

## 3. Complete concise-procedure coverage inventory

| # | Source procedure | Printed / PDF pages | Current coverage |
|---|---|---|---|
| 1 | Engine Failure During Takeoff Roll | 3-6 /72 | Represented: `engine-out-takeoff` |
| 2 | Engine Failure Immediately After Takeoff | 3-6 /72 | Represented: `engine-out-after-takeoff` |
| 3 | Engine Failure During Flight (Restart Procedures) | 3-7 /73 | Represented: `engine-out-flight` |
| 4 | Emergency Landing Without Engine Power | 3-8 /74 | Represented: `landing-no-power` |
| 5 | Precautionary Landing With Engine Power | 3-8 /74 | Represented: `landing-with-power` |
| 6 | Ditching | 3-9 /75 | Represented: `ditching` |
| 7 | During Start On Ground (Fires) | 3-10 /76 | Represented: `engine-fire-start` |
| 8 | Engine Fire In Flight | 3-11 /77 | Represented: `engine-fire-flight` |
| 9 | Electrical Fire In Flight | 3-11–3-12 /77–78 | Represented: `electrical-fire` |
| 10 | Cabin Fire | 3-12 /78 | OMITTED |
| 11 | Wing Fire | 3-13 /79 | OMITTED |
| 12 | Inadvertent Icing Encounter During Flight | 3-14 /80 | OMITTED |
| 13 | Static Source Blockage (Erroneous Instrument Reading Suspected) | 3-15 /81 | OMITTED |
| 14 | Excessive Fuel Vapor — Fuel Flow Stabilization Procedures | 3-15 /81 | OMITTED |
| 15 | Landing With A Flat Main Tire | 3-16 /82 | OMITTED |
| 16 | Landing With A Flat Nose Tire | 3-16 /82 | OMITTED |
| 17 | HIGH VOLTS Annunciator Comes On or M BATT AMPS More Than 40 | 3-17–3-18 /83–84 | OMITTED |
| 18 | LOW VOLTS Annunciator Comes On Below 1000 RPM | 3-19 /85 | OMITTED |
| 19 | LOW VOLTS Annunciator Comes On or Does Not Go Off at Higher RPM | 3-19–3-20 /85–86 | OMITTED |
| 20 | Red X — PFD Airspeed Indicator | 3-21 /87 | OMITTED |
| 21 | Red X — PFD Altitude Indicator | 3-21 /87 | OMITTED |
| 22 | Red X — PFD Attitude Indicator | 3-21 /87 | OMITTED |
| 23 | Red X — Horizontal Situation Indicator (HSI) | 3-21 /87 | OMITTED |
| 24 | Autopilot or Electric Trim Failure (if installed): AP or PTRM Annunciator(s) Come On | 3-22 /88 | OMITTED |
| 25 | Display Cooling Advisory: PFD 1 COOLING or MFD 1 COOLING Annunciator(s) Come On | 3-23 /89 | OMITTED |
| 26 | Vacuum System Failure: LOW VACUUM Annunciator Comes On | 3-23 /89 | OMITTED |
| 27 | High CO Level Advisory: CO LVL HIGH Comes On / Remains On | 3-24 /90 | OMITTED |

### Missing content in the 18 absent families

These are source-content inventory summaries, preserving condition, sequence, timing and note/warning distinctions where relevant. They are not an independently validated operational checklist.

#### O01. Cabin Fire — 3-12 / PDF 78

All eight steps are absent: standby battery OFF; master ALT/BAT OFF; cabin vents CLOSED to avoid drafts; cabin heat/air OFF, controls fully in, to avoid drafts; activate extinguisher if available; after complete extinguishment, open cabin vents; turn cabin heat/air ON, controls fully out, after complete extinguishment; land as soon as possible to inspect damage.

**Absent WARNING** between extinguisher and ventilation actions: after using the extinguisher, ensure the fire is extinguished before using exterior air to remove smoke. The existing Electrical Fire procedure has overlapping actions but is not a substitute for Cabin Fire, especially because the source adds a landing/inspection instruction here.

#### O02. Wing Fire — 3-13 / PDF 79

All four steps absent: LAND/TAXI lights OFF; NAV light OFF; STROBE light OFF; PITOT HEAT OFF.

**Absent NOTE:** sideslip to keep flames away from the fuel tank and cabin; land as soon as possible; use flaps only as required for final approach and touchdown. These four numbered source steps are bold immediate-action items.

#### O03. Inadvertent Icing Encounter During Flight — 3-14 / PDF 80

All 14 numbered steps absent:

1. Pitot heat ON.
2. Turn back or change altitude to a temperature less conducive to icing.
3. Cabin heat ON, fully out.
4. Defroster outlets OPEN for maximum windshield airflow.
5. Adjust cabin air for maximum defroster heat/airflow.
6. Watch for induction-filter icing: falling RPM may indicate ice obstruction; adjust throttle to hold RPM and mixture for changes in power.
7. Plan nearest-airport landing; choose suitable off-airport site if buildup is extremely rapid.
8. At 0.25 in or more leading-edge accumulation, anticipate much higher power requirements, higher approach/stall speeds and longer landing roll.
9. Leave flaps retracted; severe tail ice plus changed wing wake from flap extension can reduce elevator effectiveness.
10. Open left window and, if practical, scrape windshield ice for landing visibility.
11. Use forward slip on approach if needed for visibility.
12. Approach 65–75 KIAS according to ice accumulation.
13. Land in a level attitude.
14. Avoid missed approaches where possible because climb capability is severely reduced.

Steps 1–5 are bold immediate-action text; subsequent descriptive material is inside numbered steps rather than separate NOTE boxes. No source caution/warning label appears on this page.

#### O04. Static Source Blockage — 3-15 / PDF 81

Trigger text “Erroneous Instrument Reading Suspected” absent. All four steps absent: alternate static valve ON/fully out; cabin vents CLOSED; cabin heat and cabin air ON/fully out; consult Section 5 Figure 5-1 Sheet 2 alternate-static airspeed calibration corrections. First step is bold immediate-action text. Current normal preflight ALT STATIC check does not cover this failure procedure.

#### O05. Excessive Fuel Vapor / Fuel Flow Stabilization — 3-15 / PDF 81

Trigger absent: fuel-flow fluctuations of at least 1 GPH or power surges. All four steps absent: fuel pump ON; adjust mixture for smooth running; select opposite tank if vapor symptoms continue; fuel pump OFF after fuel flow stabilizes. Each condition is scoped to its associated action; there is no labeled NOTE on this concise page.

#### O06. Flat Main Tire Landing — 3-16 / PDF 82

All four steps absent: normal approach; flaps FULL; touch good main tire first and use aileron to keep weight off the flat tire as long as possible; maintain directional control, braking with the good wheel as required. Both control techniques are source parenthetical continuations of their steps.

#### O07. Flat Nose Tire Landing — 3-16 / PDF 82

All four steps absent: normal approach; flaps as required with explicit speed/configuration lines (85–110 KIAS for UP–10°, below 85 KIAS for 10°–FULL); touch down on mains and hold nosewheel off as long as possible; after nosewheel contact hold full up-elevator as speed decays to a stop.

#### O08. HIGH VOLTS / M BATT Above 40 A — 3-17–3-18 / PDF 83–84

All three main steps, all eleven load-shedding substeps and all notes absent:

1. MASTER ALT only OFF.
2. Reduce electrical load immediately, in source order: avionics BUS 1 OFF; pitot heat OFF; beacon OFF; landing light OFF except as needed for landing; taxi OFF; nav OFF; strobe OFF; cabin 12 V power OFF; tune COM 1/NAV 1 to active frequency; select COM 1 MIC/NAV 1; avionics BUS 2 OFF, **keep ON in clouds**.
3. Land as soon as practical.

**Notes/descriptive text absent:**

- Main battery powers main/essential buses until M BUS drops below 20 V, after which standby automatically supplies essential bus for at least 30 minutes.
- Select COM 1 MIC/NAV 1 and tune before BUS 2 OFF: leaving COM 2 MIC/NAV 2 selected prevents COM/NAV tuning after BUS 2 is off.
- Source substep j repeats that COM 2 MIC/NAV 2 become inoperative after BUS 2 OFF.
- BUS 2 OFF disables autopilot, audio panel, COMM 2, NAV 2, transponder and MFD.
- Before extending flaps ensure a successful landing is possible; flap motor imposes a large electrical load.

The existing electrical-fire procedure addresses a different trigger and does not cover this load-shedding plan.

#### O09. LOW VOLTS Below 1000 RPM — 3-19 / PDF 85

All steps absent: set throttle 1000 RPM; verify LOW VOLTS annunciator OFF; **if it remains on at 1000 RPM**, require electrical-system inspection by authorized maintenance before next flight. That last conditional heading and maintenance requirement are absent.

#### O10. LOW VOLTS at Higher RPM — 3-19–3-20 / PDF 85–86

All nine main steps, all eleven load-shedding substeps, condition and notes absent. Source initial sequence: MASTER ALT only OFF; check ALT FIELD breaker IN; MASTER ALT/BAT ON; check LOW VOLTS OFF; check M BUS at least 27.5 V; check M BATT positive charging.

**If LOW VOLTS remains on:** MASTER ALT only OFF; reduce load immediately using the same a–k sequence as O 08; land as soon as practical. Source repeats the 20 V/standby ≥30 min note, select/tune COM 1/NAV 1 before BUS 2 OFF note, list of lost BUS 2 equipment, keep BUS 2 ON in clouds exception, and ensure landing before flap-extension/high-load note. These repeated notes are genuinely present in both source procedures.

#### O11–O14. Four Red-X Instrument Failures — 3-21 / PDF 87

All four two-step procedures absent. Each begins by checking ADC/AHRS breakers on ESS BUS and AVN BUS 1; if open reset/close, and **do not reset again if it opens again**. This source-specific reset instruction belongs to these failures and must not be generalized to electrical fire.

The second step differs:

- **O 11 Airspeed:** use standby airspeed indicator.
- **O 12 Altitude:** check standby altimeter has current barometric setting, then use it for altitude.
- **O 13 Attitude:** use standby attitude indicator.
- **O 14 HSI:** use non-stabilized magnetic compass for heading.

No labeled NOTE, WARNING or CAUTION is printed on this page. Current preflight red-X checks do not cover failure recovery or fallback-instrument use.

#### O15. Autopilot / Electric Trim Failure — 3-22 / PDF 88

Conditional applicability “if installed” and AP/PTRM annunciator trigger absent. All five steps absent: firmly grasp control wheel to regain control; press and hold A/P TRIM DISC throughout recovery; adjust elevator trim manually as necessary; open/pull AUTO PILOT breaker; release A/P TRIM DISC. Source steps 1–4 are bold immediate actions.

**Absent WARNING:** do not re-engage autopilot after autopilot/autotrim/manual electric-trim malfunction until the cause is corrected. The normal after-start autopilot disconnect test is not emergency coverage.

#### O16. Display Cooling Advisory — 3-23 / PDF 89

Trigger and both response branches absent. Source first reduces cabin heat (minimum preferred) then checks forward avionics fan by feeling for airflow at the glareshield screen.

- If forward fan failed: standby battery OFF, **unless needed for emergency power**.
- If either cooling annunciator has not cleared within 3 minutes **or both appear**: standby battery OFF and land as soon as practical.

Both branches are separately labeled conditions; do not combine their differing exceptions or trigger thresholds. No labeled NOTE on this page.

#### O17. Vacuum System Failure — 3-23 / PDF 89

LOW VACUUM trigger and single bold action absent: inspect VAC on EIS ENGINE page, confirm pointer within green-band limits.

**Absent CAUTION:** if the pointer is out of green in flight or standby attitude indicator shows its gyro flag, do not use that standby attitude indicator for attitude information. This is distinct from ordinary run-up VAC checking.

#### O18. High Carbon Monoxide Advisory — 3-24 / PDF 90

All five steps absent, grouped under initial and persistent annunciation conditions. Initial: cabin heat OFF/fully in; cabin air ON/fully out; cabin vents OPEN; windows OPEN, with 163 KIAS maximum window-open speed. Persistent: land as soon as practical. Source first three steps are bold immediate actions. The fifth continues step numbering, so this audit treats both headings as one family.


## 4. General emergency guidance and reference data

| Reference | Material | Current status and nature |
|---|---|---|
| 3-5 / PDF71 | Continued control of the airplane and maneuvering for a successful landing take priority in any emergency. | No general priority statement on current emergency cards. Operational principle, not an additional switch action. |
| 3-5 / PDF71 | Maneuvering speed by weight: 105 KIAS at 2550 lb, 98 KIAS at 2200 lb, 90 KIAS at 1900 lb. | Entire three-row reference absent. Reference information; do not turn into a single unqualified speed. |
| 3-5 / PDF71 | Engine-failure-after-takeoff and landing-without-power 70 KIAS flaps UP / 65 KIAS flaps 10°–FULL; max glide 68 KIAS; precautionary powered landing 65 KIAS. | These speeds are already represented in `engine-out-after-takeoff`, `landing-no-power`, `engine-out-flight`, and `landing-with-power`. No new speed omission. |
| 3-6 / PDF72 | Boldface in POH's Emergency Procedures Checklist identifies immediate-action items to commit to memory. | Current general bold/medium challenge-response styling does not encode this specific POH distinction. Cross-cutting semantic/style gap; it requires mapping the POH's actual emphasized items, not declaring every current bold item a memory item. |
| 3-5 / PDF71 | Optional/supplemental-equipment emergency procedures are in Section 9. | Scope pointer, no operational action. Section 9 reviewed below. Prevention/preflight/weather-planning introductory rationale also need not become card items. |

### Amplified additions to the nine represented procedures

| Reference | Existing procedure(s) | Absent or incomplete operational content | Background/overlap to keep separate |
|---|---|---|---|
| 3-25 / PDF91, Engine Failure | `engine-out-takeoff` | Stop on the **remaining runway** is not stated explicitly. | Current throttle IDLE/brakes APPLY already implement stopping; the text explains the remaining shutdown steps add safety. This is context, not a wholly missing procedure. |
| 3-25 / PDF91, Engine Failure | `engine-out-after-takeoff` | Only **small direction changes to avoid obstructions**, and securing fuel/ignition assumes **adequate time before touchdown**. | STRAIGHT AHEAD now present. The explanation that altitude/airspeed are seldom enough for a 180° glide back is absent background that qualifies maneuver choice; do not replace the source's nuanced guidance with a new numerical turnback rule. |
| 3-25 / PDF91, Engine Failure | `engine-out-flight`, `landing-no-power` | Prioritize continued flight; establish best glide promptly; glide toward a suitable area while identifying cause; **attempt restart only if time permits**; if restart fails, complete forced landing without power. | Current 68 KIAS and restart switch sequence exist, but landing-area selection, time limitation, and explicit restart-fails transition are not encoded. |
| 3-26 / PDF92, Figure 3-1 Maximum Glide | `engine-out-flight` | Figure's conditions **propeller windmilling, flaps UP, zero wind** are not attached to a glide-range reference. | 68 KIAS exists. The height-above-terrain versus ground-distance graph is absent, and is reference material rather than a required new checklist action. The graph was visually inspected; these conditions are in the image, absent from text extraction. |
| 3-27 / PDF93, Forced Landings | `landing-no-power` | Select suitable field; transmit Mayday on **121.5 MHz**, giving location/intentions and squawk **7700**. | Similar radio instruction exists only under `ditching`; that does not cover land forced landing. |
| 3-27 / PDF93, Forced Landings | `landing-with-power` | Fly over landing area at a safe but low altitude to inspect **obstructions and surface conditions** before attempting off-airport landing. | Also overlaps missing concise precautionary-landing field-selection/inspection item, so count once in combined report. |
| 3-27 / PDF93, Forced Landings | `ditching` | Explicitly **avoid a landing flare**. | Reason: water height is difficult to judge. Existing level attitude/established descent touchdown is related, but does not explicitly state no flare. Heavy-object security, coat cushioning, Mayday, and power-off airspeed/flap alternatives are now present and should not be reported missing. |
| 3-27 / PDF93, Forced Landings | `landing-no-power`, `landing-with-power`; forced-landing transitions generally | **Do not switch MASTER, AVIONICS, or STBY BATT off until landing is assured.** | Current shutdown steps lack this condition. Explanation that early shutdown disables electrical systems is rationale. Do not transplant this to immediate fire isolation actions; source context is forced landing. |
| 3-27 / PDF93, Forced Landings | `landing-no-power`, `landing-with-power` | **Activate ELT before completing a forced landing**, especially remote/mountainous terrain. | ELT activation exists in current `ditching`, but not land-based forced landings. Section 9 adds model-specific operation and verification. |
| 3-28 / PDF94, Fires | `engine-fire-start` / prestart context | If excessive priming has left a fuel puddle, **push airplane away before another start attempt**. | Flooding and tailpipe-flame mechanism are background. This is an upstream prevention action, not a step to insert during active fire response without its condition. |
| 3-28 / PDF94, Fires | `engine-fire-flight` | **Do not attempt to restart the engine** after the fire procedure. | Forced landing already exists. This is a clear additional operational prohibition absent from the current card. |
| 3-28 / PDF94, Fires | `electrical-fire` | No distinct new action in the amplified paragraph. | Burning-insulation smell as a typical first sign is absent recognition background. The statement that the checklist should eliminate the fire is rationale, not an additional step. |

## 5. Amplified procedures and operating branches missing from the cards

Every topic below has no current dedicated procedure ID. Some also have concise Section 3 checklists, which overlap Section 3 of this report and must not be counted as different failures simply because they have amplified discussion. Summaries here identify content to evaluate; they are not substitute cockpit checklists.

| Source topic and reference | Missing operational material | Distinction / connection |
|---|---|---|
| **Landing Without Elevator Control**, 3-28 / PDF94 | Establish approximately **65 KIAS**, **20° flaps** using throttle/trim; then leave trim fixed and control glide angle with power. During flare adjust trim toward full nose-up while adjusting power to bring airplane horizontal for touchdown; close throttle at touchdown. | Entire special landing procedure absent; `landing-with-power` does not cover elevator failure. Source explains power reduction's nose-down/nosewheel-touchdown tendency. Preserve sequence-dependent fixed-trim versus flare-trim instructions. |
| **Emergency Operation in Clouds**, 3-29 / PDF95 | Vacuum failure: rely on PFD AHRS attitude/heading; AHRS failure: rely on standby attitude indicator and magnetic compass; **manually fly** because autopilot will not operate with failed AHRS. | Entire instrument-failure context absent. Vacuum failure alone does not disable AP with valid HDG/GPS/NAV inputs. Related to missing concise AHRS/vacuum procedures; do not merge the two failures. |
| **Executing a 180° Turn in Clouds (AHRS Failed)**, 3-29 / PDF95 | Five-step course reversal: note magnetic heading; use standby attitude for **15° left bank for 60 seconds**, feet off rudder, maintain altitude; level and verify reciprocal once compass settles; if needed use wings-level rudder corrections; maintain altitude/airspeed cautiously, roll pointer/index aligned. | Entire amplified-only procedure absent. Source explicitly assumes pilot not proficient in instrument flight and AP not engaged. Those assumptions matter; this is not a generic instrument-turn procedure. |
| **Emergency Descent Through Clouds (AHRS Failed)**, 3-30 / PDF96 | When reversal to VFR is impractical, obtain ATC clearance if possible; choose E/W heading; full rich, pitot heat ON, **500–800 ft/min**, trim **80 KIAS**; standby attitude wings level, cautious compass/rudder corrections, resume normal cruise after emerging. | Entire amplified-only procedure absent. Source rationale is reduced magnetic-compass sensitivity E/W and unavailable AP with AHRS failed. |
| **Recovery From Spiral Dive in Clouds (AHRS Failed)**, 3-31 / PDF97 | Idle throttle; feet off rudder; level wings using standby attitude; cautiously reduce to **80 KIAS** with elevator; trim 80-KIAS glide; maintain level wings/heading; resume emergency cloud-descent procedure, then normal cruise when clear. | Entire eight-step amplified-only procedure absent. Must not confuse with spin recovery below. |
| **Inadvertent Flight Into Icing Conditions**, 3-31 / PDF97 | Escape by turnback/altitude change; pitot heat ON **until safely clear**. If power loss due to induction/reference-tube icing, position throttle for **maximum RPM (possibly retarding it)**, then adjust mixture for maximum RPM. | All icing procedure absent. Escape/pitot items overlap concise 3-14; throttle/mixture power-loss branch is added amplified guidance. Ice-filter/reference-tube mechanism and prohibition are contextual explanation/limitation. |
| **Static Source Blocked**, 3-32 / PDF98 | Suspect erroneous ASI/altimeter/VSI: alternate-static valve ON; consult Section 5 Fig 5-1 sheet 2 calibration corrections. | Whole procedure absent (also concise 3-15). Additional reference: maximum variation **11 kt** and **50 ft**, all windows closed. These values are differences, not blanket corrections to apply. |
| **Spins**, 3-32 / PDF98 | Six-step recovery: throttle IDLE, ailerons NEUTRAL, full opposite rudder; immediately after rudder stop move wheel briskly forward enough to break stall; hold until rotation stops; neutralize rudder and recover smoothly. | Entire amplified-only emergency procedure absent. Need preserve sequencing and full-down-elevator possibility at aft CG. |
| **Spins NOTE**, 3-32 / PDF98 | If rotation direction is hard to determine, use **magenta turn-rate vector at top of HSI**, apply opposite rudder to that vector. | HSI compass card rotates opposite; do not use card rotation as the rudder-direction cue. Operational note and explanatory contrast both absent; tied to missing spin procedure. |
| **Spark Plug Fouling**, 3-33 / PDF99 | Momentary individual-magneto check; lean to recommended cruise mixture; if not clear after several minutes try richer; if unresolved nearest airport for repairs, BOTH unless extreme roughness requires single magneto. | Entire roughness branch absent. Recognition of deposits/single-magneto power loss is diagnostic context. `engine-out-flight` restart is not an equivalent. |
| **Magneto Malfunction**, 3-33 / PDF99 | Identify bad magneto via L/R; vary power and enrichen to assess operation on BOTH; otherwise good magneto and nearest airport for repair. | Entire branch absent. Sudden roughness/misfiring is recognition context. |
| **Idle Power Engine Roughness**, 3-33 / PDF99 | Lean mixture to improve rich low-speed roughness in flight; leaning may also be necessary for restart after low-speed power loss; **nearest airport for repair if adjustment is required**. | Entire branch absent. Full-rich normal landing cue and ordinary cruise leaning do not cover it. Printed heading references AD 2001-06-17(d)(3); this audit merely reports supplied POH text, without claiming current AD applicability. |
| **Engine-Driven Fuel Pump Failure**, 3-34 / PDF100 | If failed, immediately auxiliary FUEL PUMP ON; terminate flight as soon as practical and repair. | `engine-out-flight` has pump ON and re-enable if flow drops to zero, but not diagnosis or terminate-flight instruction. Diagnostic cue: sudden fuel-flow reduction immediately before power loss with adequate fuel in selected tank. |
| **Excessive Fuel Vapor**, 3-34 / PDF100 | Pump ON, mixture for smooth operation, opposite tank if symptoms persist; pump OFF once flow stabilizes, readjust mixture. | Entire procedure absent (also concise 3-15). Recognition threshold **flow fluctuations >1 gal/hr**, warm/high/prolonged-taxi context, possible surges/power loss. Do not treat as identical to failed mechanical pump. |
| **Low Oil Pressure**, 3-35 / PDF101 | Confirm annunciation with oil-pressure indication. If pressure/temperature remain normal, nearest airport to determine cause. If total pressure loss plus temperature rise, **reduce power immediately**, select forced-landing field, minimum power to reach it. | Entire two-branch procedure absent; routine oil check and generic engine-out list do not cover it. Sensor/relief-valve possibility and impending-failure explanation are diagnostic rationale. |
| **Excessive Rate of Charge**, 3-36 / PDF102 | If overvoltage protection fails and main bus exceeds approximately **31.75 V**, MASTER ALT OFF, shed unnecessary electrical equipment, terminate as soon as practical. | Entire non-fire electrical procedure absent (also concise 3-17/18). Recognition/background: after 30 min cruise charge normally <5 A; persistent higher current can overheat battery. Do not replace concise >40-A trigger with this different monitoring discussion. |
| **Insufficient Rate of Charge**, 3-37 / PDF103 | MASTER ALT OFF → ALT FIELD breaker CHECK IN → MASTER ALT ON; verify charge and LOW VOLTS clear. If LOW VOLTS returns, **do not repeat** re-energizing attempts; shed loads promptly, land as soon as practical. | Entire non-fire low-voltage procedure absent (also concise 3-19/20). Electrical-fire breaker DO NOT RESET is not a substitute; failure conditions differ. |
| **Insufficient Rate of Charge continued**, 3-38 / PDF104 | Where practical conserve main battery by MASTER ALT/BAT OFF and ESS BUS on standby; preserve main battery for later flaps/landing light. | Added operational conservation option absent. ESS BUS-only/XPDR unavailable is an important consequence, not generic all-electrical-failure advice. |
| **Low-RPM LOW VOLTS NOTE**, 3-38 / PDF104 | Higher RPM may clear annunciation under heavy low-RPM load; **verify positive M BATT AMPS at higher RPM**. | Absent emergency diagnostic note; overlaps concise below-1000-RPM case. It is a named NOTE in the source and should not be promoted merely for containing an instruction. |
| **High CO Level Annunciation**, 3-39/40 / PDF105 | **Smelled exhaust or symptoms**, as well as warning while heater in use, trigger immediate CABIN HT OFF and CO emergency procedure. | Entire CO procedure absent (also concise 3-24). Symptoms (blurred thinking, unease, dizziness, headache, unconsciousness), heater-leak mechanism, and 50-ppm alarm/reset behavior are recognition/system background. The amplified trigger is broader than waiting for an annunciator. |
| **Windshield Damage**, 3-39/40 / PDF105 | Opening side windows may reduce performance loss after windshield opening; maneuver to nearest airport; if impossible prepare off-airport powered landing or ditching. | Entire amplified-only procedure absent. Opening side windows is a conditional possibility, not a universal mandatory response to every crack. |

## 6. Supplied Section 9 supplements

Main TOC (vii/viii / PDF7) separates Sections 3 and 9. Section 3 introduction (3-5 / PDF71) explicitly points to equipment supplements; Section 9 introduction (9-1/9-2 / PDF309) establishes applicability to installed equipment. Supplied Log of Approved Supplements (Log1/Log2 / PDF311, dated 20 Dec 2007) lists five supplements and provides no aircraft-specific installed-equipment markings. This inventory checks the five supplied supplements, not outside or later revisions.

| Supplement | Emergency subsection | Added material absent from cards |
|---|---|---|
| **1, Artex ME406 ELT** | S1-7 / PDF319 | For necessary forced landing, remote ON **before landing**; red light flashing and aural warning. After landing when rescue is needed: confirm energized via flashing light/remote ON; listen for aural warning; **only if safe from fire/explosion and COM works**, tune 121.5 to verify ELT tone, then de-energize COM to conserve battery; ensure antenna unblocked. If remote damaged, cycling requires switch on ELT itself. After rescue remote ARM; if remote fails, switch on ME406 to **ARM**. No postlanding/rescue procedure exists in current cards. Ditching ELT ACTIVATE only partially overlaps. |
| **2, Artex C406-N ELT** | S2-7 / PDF327 | Same basic prelanding/verification/rescue sequence, except fallback after-rescue switch on C406-N is **OFF**, not ME406's ARM. Select procedure according to installed ELT; do not combine model-specific switch positions. |
| **3, Bendix/King KR87 ADF** | S3-8 / PDF336 | Explicitly **no change** to airplane emergency procedures. No missing supplementary emergency checklist to add. |
| **4, Winterization Kit** | S4-6 / PDF346 | Explicitly **no change** to emergency procedures. |
| **5, JAR-OPS Operational Eligibility** | S5-5/S5-6 / PDF351 | Explicitly **no change** to emergency procedures. |

Supplement Normal Procedures sections contain accidental ELT activation reset/test and ADF operating notes, but those are outside this emergency-subsection scope; they have not been reported as new emergency omissions. Likewise Section 3 references Section 4 spin material and Section 5 alternate-static calibration; the referenced whole sections have not been re-audited here.

## 7. How to choose the next changes

First decide which missing procedures the two emergency sides should cover. A compact personal checklist can deliberately omit material, but the decisions should be explicit. The count above is not a recommendation to force all 27 families and amplified instructions onto two sides.

A useful first discussion set is **autopilot/electric-trim failure, cabin and wing fires, CO response, and spin recovery**: all are currently absent and introduce responses not supplied by an engine-failure checklist. Icing, electrical-power loss/load shedding, instrument failure, rough running, and low oil pressure are also substantial coverage gaps. Their inclusion depends on the aircraft equipment, intended operations, and available space. This grouping is a design/review judgment, not a frequency ranking or an externally mandated priority list.

For the procedures already printed, distinguish three decisions:

1. **Contrary action or missing operational content:** electrical-fire OFF/ON; start-fire duration and continuation; powered-landing missing actions; amplified no-restart-after-engine-fire; forced-landing communications/ELT. Some were previously discussed but not implemented. Revisit only if the user chooses to.
2. **Previously retained wording:** C7 and C8, and the specified C1 material. Cataloged for completeness; no automatic reopening or change.
3. **Extra descriptive text:** full-in/full-out instructions, pilot/passenger wording, draft/combustion explanations, long diagnostic background. These can remain abbreviated unless a fuller response materially improves this card's usability or alignment.

If retaining two emergency sides, reserve their limited space for the selected actions, relevant conditions, and essential warnings/notes. Keep long background paragraphs and performance graphs in a separate reference document or the POH. For lengthy non-fire electrical faults, a separate systems/abnormal reference card is a possible deliberate tradeoff; it should not be silently implied by the existing Electrical Fire heading.

No fonts need to be reduced just to make the initial landing regrouping. If new content causes overflow, choose scope or placement explicitly rather than dropping warnings, attaching instructions to the wrong condition, or making the text smaller without review.

## Verification record

The review used the current source and printed emergency pages, not the superseded audit baseline. Section 3 contents, introduction, all concise procedures, the full amplified text, and all five supplied supplements' emergency subsections were checked. Source page images were used to distinguish bold immediate actions, ordinary numbered steps, conditional headings, NOTE/WARNING/CAUTION blocks, and the glide graph's embedded assumptions. The current two emergency PDF sides were visually inspected and their remaining column heights measured.

The concise inventory has 27 entries: 9 represented and 18 absent. The two CO headings are one procedure family; if counted separately, the literal heading counts become 28 and 19. Amplified-only procedures and ELT supplements are intentionally additional inventories. Cross-references to Section 4 spins, Section 5 calibration, and Section 7 systems are identified where relevant; those whole sections and external Garmin publications were not re-audited line by line. No claim is made that a 2007 generic Information Manual proves applicability to every installed aircraft configuration.

This report is a decision catalog, not a newly approved cockpit procedure. Checklist YAML, layout, and PDF remain unchanged during this pass.
