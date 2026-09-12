#import "../theme.typ": theme
#import "../components.typ": *
#let mode = sys.inputs.at("case", default: "wrap")
#set page(width: 220pt, height: 400pt, margin: 12pt)
#set text(font: theme.font, size: theme.body-size, weight: theme.body-weight,
  hyphenate: false, fallback: false, top-edge: "cap-height", bottom-edge: "baseline")
#set par(leading: 3pt, spacing: 0pt)
#set block(spacing: 0pt)
#let item = (id: "synthetic-row", type: "check",
  challenge: "Example control with a long label",
  qualifier: "only under this example condition",
  response: "KEEP EVERY WORD IN THIS LONG EXAMPLE RESPONSE",
  notes: ("A supporting note remains attached below its response.",))
#if mode == "wrap" {
  fit-region(check-row(item, 150pt, theme), 150pt, 300pt, "wrapped example")
} else if mode == "overflow" {
  fit-region(stack(dir: ttb, spacing: 4pt,
    ..range(10).map(_ => check-row(item, 150pt, theme))),
    150pt, 50pt, "deliberately overfull column")
} else if mode == "word" {
  let bad = item + (response: "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",)
  check-row(bad, 70pt, theme)
} else if mode == "title" {
  section((title: "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ",
    category: "normal", blocks: (item,)), 100pt, theme)
} else if mode == "title-wrap" {
  section((title: "ENGINE OUT - AFTER TAKEOFF", category: "emergency", blocks: ()), 100pt, theme)
} else if mode == "duplicate" {
  validate-procedures((example: (blocks: (item, item),)))
} else if mode == "missing" {
  procedure-column(("not-found",), (:), 150pt, 300pt, "missing example", theme)
} else if mode == "nested" {
  render-block((type: "branch", id: "outer", condition: "OUTER CONDITION", blocks: (
    (type: "subprocedure", id: "inner", title: "INNER GROUP", blocks: (item,)),
  )), 190pt, theme)
} else if mode == "note-word" {
  note("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ", 70pt, theme)
} else if mode == "category" {
  section((title: "EXAMPLE", category: "unknown", blocks: (item,)), 190pt, theme)
} else {
  panic("Unknown test case")
}
