#import "theme.typ": theme as t
#import "components.typ": validate-procedures
#import "sheet.typ": sheet
#let plan = yaml("layout/kneeboard.yaml")
#let data = yaml("content/procedures.yaml")
#assert(data.schema_version == 1, message: "Unsupported checklist schema version")
#validate-procedures(data.procedures)
#let procedures = data.procedures
#set document(title: "Cessna 172S G1000 Checklist",
  description: "Personal flight checklist: two double-sided kneeboard cards.")
#set page(width: plan.width_pt * 1pt, height: plan.height_pt * 1pt,
  margin: (top: plan.at("top_margin_pt", default: plan.margin_pt) * 1pt,
    x: plan.margin_pt * 1pt, bottom: plan.bottom_margin_pt * 1pt),
  footer-descent: 4pt,
  footer: context {
    let number = counter(page).get().first()
    set text(font: t.font, size: t.footer-size, weight: 500)
    let current = plan.pages.at(number - 1)
    let reverse-number = if calc.odd(number) { number + 1 } else { number - 1 }
    let other = plan.pages.at(reverse-number - 1)
    assert(current.card == other.card and current.side != other.side,
      message: "Each card needs consecutive A/B sides")
    align(center, stack(dir: ttb, spacing: 4pt,
      text(weight: 700, current.name),
      [C172S G1000],
    ))
  })
#set text(font: t.font, size: t.body-size, weight: t.body-weight,
  hyphenate: false, fallback: false, lang: "en",
  top-edge: "cap-height", bottom-edge: "baseline")
#set par(leading: t.line-leading, spacing: 0pt)
#set block(spacing: 0pt)
#for (i, page-plan) in plan.pages.enumerate() {
  if i > 0 { pagebreak() }
  sheet(page-plan, plan, procedures, t)
}
