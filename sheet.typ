#import "components.typ": procedure-column

// Placement remains explicit: never split or automatically move a procedure.
#let sheet(page-plan, geometry, procedures, t) = {
  let count = page-plan.columns.len()
  assert(count > 0, message: "A page needs at least one column")
  let gutter = geometry.column_gutter_pt * 1pt
  let body-height = (geometry.height_pt - geometry.at("top_margin_pt", default: geometry.margin_pt)
    - geometry.bottom_margin_pt - geometry.at("footer_gap_pt", default: 0)) * 1pt
  let column-width = (geometry.width_pt * 1pt - 2 * geometry.margin_pt * 1pt
    - (count - 1) * gutter) / count
  assert(column-width > 0pt and body-height > 0pt, message: "No space for columns")
  block(height: body-height, breakable: false,
    grid(columns: (column-width,) * count, column-gutter: gutter,
      ..page-plan.columns.enumerate().map(((i, entries)) => {
        procedure-column(entries, procedures, column-width, body-height,
          page-plan.name + "/column-" + str(i + 1), t,
          stretch-min-fill: geometry.at("stretch_min_fill", default: none))
      })))
}
