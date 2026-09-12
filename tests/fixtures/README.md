# Independent content expectations

`reference-changes.json` contains the reviewed exceptions to the original checklist PDF:

- `replacements`: each `before` passage must occur exactly once in its original procedure; replace it with `after`.
- `endings`: verify the original procedure ends with `after`, then append the listed lines.
- `additions`: independent expected text for procedures absent from the original PDF.

Each text value is an array of readable lines. Whitespace is ignored during comparison, so line breaks here describe content rather than typesetting. Leaders are removed by the PDF extractor; numbers, punctuation, capitalization, and order remain significant.

These expectations were extracted from the previously reviewed test literals at commit `9174e4a`, with whitespace added for readability. They are deliberately independent of `content/procedures.yaml`. Do not regenerate them automatically from production content or the rendered PDF. After an intentional content change, review the original/source wording, update only its expected exception, and record the decision in [Content decisions](../../docs/content-decisions.md).

The original PDF contains a shorter in-flight engine-out duplicate. Its title remains recognized by the reference parser solely to split that historical source column correctly; it is not a maintained procedure or renderer variant.
