# Content decisions

This is the current decision record, consolidated during repository cleanup after commit `9174e4a`. Update this file when decisions change; leave the two historical audit reports as baseline evidence. Procedure text lives in [procedures.yaml](../content/procedures.yaml), and independent test exceptions live in [reference-changes.json](../tests/fixtures/reference-changes.json).

## References and review policy

The initial transcription came from [original.pdf](../original.pdf). The supplied POH reference is the local [C172S G1000 Information Manual](/Users/sam/Downloads/C172S-G1000-POH.pdf), original issue 20 December 2007, NAV III / GFC 700, 172SPHBUS-00 / 172SIMBUS-00. Its SHA-256 is `11bb6be70757984fc7b05a69bc8242bdcbc79cf73604c5837364bd8013aa9b0a`. The POH itself is not stored in this repository. Page references below use printed page numbers.

The user's review rule is to change POH-covered material only to improve alignment with that source, while preserving items that already match. Later explicit user choices take precedence. The retained differences below are deliberate decisions, not outstanding instructions to correct them. The review does not establish applicability to a particular aircraft or complete reconciliation with its POH.

## Implemented changes

| Area | Current decision | Reference |
|---|---|---|
| Emergency airspeeds (P1) | After-takeoff engine failure and no-power landing show separate action responses: 70 KIAS with flaps UP; 65 KIAS with flaps 10°–FULL. | POH 3-6, 3-8 |
| Electrical restoration (C1, copied rows only) | Replace the accidentally copied battery-test rows with Circuit Breakers CHECK (for open circuits, do not reset), MASTER ON, STBY BATT ARM, AVIONICS BUS 1 ON, AVIONICS BUS 2 ON. | POH 3-12 |
| Magneto drop (C3) | 150 RPM maximum drop; retain the 50 RPM differential. | POH 4-16, 4-29 |
| Main-bus voltage (C4) | 1.5 volts or less. | POH 4-12 |
| Takeoff flaps (C9) | UP–10°, retaining the 10° preference. | POH 4-17–4-18 |
| Cruise | Add RPM to 2100–2700. | POH 4-19 |
| Takeoff-roll engine failure | Add MASTER (ALT & BAT) OFF after STBY BATT OFF. | POH 3-6 |
| After-takeoff engine failure | Add Cabin Door UNLATCH and Land STRAIGHT AHEAD at the end. | POH 3-6 |
| Landing With Power | Add the second Airspeed 65 KIAS after FULL flaps. Add Mixture Control IDLE CUTOFF and MAGNETOS Switch OFF between Touchdown and Brakes. | POH 3-8 |
| Ditching | Add 20°–FULL flap range, no-power approach note, Cabin Doors UNLATCH, Touchdown, ELT ACTIVATE, Airplane EVACUATE, and the pressure-equalization note. Use FT/MIN. Subsequent wording choices are below. | POH 3-9 and user edits |
| Cabin Fire | Add the procedure. Ventilation responses after extinguishment are Cabin Vents OPEN and CABIN HT / CABIN AIR ON. Subsequent presentation choices are below. | POH 3-12 and user edits |
| Wing Fire | Add the four switch-off actions and final Land AS SOON AS POSSIBLE. | POH 3-13 and user edits |

### Subsequent user-selected simplifications

- **Ditching:** Touchdown is **SLOW AS POSSIBLE**, replacing earlier level-attitude wording. This is a user-selected departure from the supplied POH. Airplane is **EVACUATE**. Remove the Approach direction item, face cushioning, and life vests/raft. Keep the no-power approach and pressure-equalization notes. Intermediate conditional and one-line Approach treatments were rejected.
- **Cabin Fire:** Remove the ventilation WARNING paragraph. Replace the two repeated “When sure that fire is completely extinguished” notes with one **IF FIRE HAS BEEN EXTINGUISHED** condition covering the two ventilation actions. Remove “To inspect for damage” below Land.
- **Wing Fire:** Remove the entire sideslip/flap explanatory note. Express its landing instruction as the final **Land … AS SOON AS POSSIBLE** row.

## Reviewed and retained

| Area | Decision |
|---|---|
| Priming presentation (P2) | Reverted the proposed presentation change. Keep Full Rich and “Approx. 3–5 seconds until stable flow.” |
| Remaining Electrical Fire differences (C1) | Keep the existing warning omission, abbreviated conditions, and second CABIN HT / CABIN AIR OFF response. Authorization was narrowed to replacing the copied restoration rows only. This differs from the later Cabin Fire ON response. |
| STBY BATT test (C2) | Keep the existing 10-second wording. |
| Warm-engine priming and engine-start condition (C5–C6) | Keep the existing omissions/wording. |
| In-flight restart (C7) | Keep abbreviated conditions and supporting notes. |
| Landing MASTER timing (C8) | Keep existing wording without the additional “when landing is assured” condition. |
| Engine-failure wording review | Keep abbreviated titles, physical-control travel wording, restart notes, and amplified guidance omissions discussed in the follow-up review. |
| Normal-procedure review | Retain the reviewed differences for alternate static valve, empennage controls, avionics fans, autopilot checks, engine-start verification/sequence, and shutdown. |

## Placement and presentation decisions

- Use two duplex half-Letter cards with compact original type sizes. Larger-type formats required too many cards for the user's preference.
- Keep the complete in-flight engine-out procedure once. Keep After Landing and Shutdown only on the normal card. Remove Airport Information and the obsolete shortened engine-out variant.
- Group no-power landing, powered landing, and Ditching in that order alongside engine failures.
- Order fires: start, in-flight engine, electrical, cabin, wing. The first two occupy the left column, the remaining three the right.
- Keep section/aircraft footer text; omit page numbers and reverse-side references. Balance conditional-heading whitespace and add space around inline boxes.

## Remaining review

The current cards represent **11 of the 27 concise Section 3 procedure families** counted by the emergency audit; **16 remain absent**. This is separate from the 27 total authored normal and emergency procedures in the repository. Amplified-only procedures and Section 9 supplements add further material outside that count.

The [emergency audit](emergency-procedure-review.md) preserves the detailed omission catalog. Its original 9-present/18-absent counts predate Cabin Fire and Wing Fire, and its landing/fire wording tables predate the changes recorded here. Use those historical findings together with this decision record.

Remaining candidates include the unreviewed fire wording and amplified guidance, whole absent emergency procedures, and C10/C11 mixture recommendations from the [focused audit](poh-note-condition-review.md). No further change to these items was authorized during repository cleanup. Previously retained differences should not be silently reopened.
