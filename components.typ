// Rendering functions accept explicit available widths. No item coordinates.
#let note(body, width, t, emphatic: false) = context {
  set text(size: t.note-size, weight: if emphatic { 700 } else { 300 }, style: "italic")
  set par(leading: t.note-leading, justify: false)
  for word in body.split(regex("\\s+")) {
    assert(measure(text(word)).width <= width, message: "Unbreakable word in note: " + word)
  }
  block(width: width, breakable: false, align(center, body))
}

#let check-row(item, width, t) = context {
  let left = item.challenge
  let qualifier = item.at("qualifier", default: none)
  let response = if qualifier == none { text(item.response) } else {
    [#text(size: t.qualifier-size, "(" + qualifier + ")")#h(2pt)#text(item.response)]
  }
  let left-width = measure(left).width
  let right-width = measure(response).width
  let single = left-width + right-width + t.leader-min + 2 * t.leader-gap <= width
  // A long response drops below its challenge as one right-aligned paragraph.
  // It keeps full-size text and every word; it never shrinks or clips.
  let row = if single {
    [#box(left)#h(t.leader-gap)#box(width: width - left-width - right-width - 2 * t.leader-gap,
      text(weight: 300, repeat(gap: 0.6pt, justify: false)[.]))#h(t.leader-gap)#box(response)]
  } else {
    stack(dir: ttb, spacing: t.response-gap,
      block(width: width, left),
      block(width: width, align(right, response)),
    )
  }
  // Measure unbreakable words too: paragraph width alone hides overlong tokens.
  for word in (item.challenge + " " + item.response).split(regex("\\s+")) {
    assert(measure(text(word)).width <= width,
      message: "Unbreakable word exceeds row width in " + item.id + ": " + word)
  }
  if qualifier != none {
    for word in qualifier.split(regex("\\s+")) {
      assert(measure(text(size: t.qualifier-size, word)).width <= width,
        message: "Unbreakable qualifier exceeds row width in " + item.id)
    }
  }
  let parts = (block(width: width, breakable: false, row),)
  for extra in item.at("notes", default: ()) {
    parts.push(note(extra, width, t))
  }
  block(width: width, breakable: false,
    stack(dir: ttb, spacing: t.note-gap, ..parts))
}

#let render-block(item, width, t) = {
  if item.type == "check" {
    check-row(item, width, t)
  } else if item.type == "note" {
    note(item.text, width, t)
  } else if item.type == "branch" or item.type == "subprocedure" {
    let boxed = item.at("boxed", default: true)
    let inner = width - if boxed { 2 * t.inset + 2 * t.outline } else { 0pt }
    let title = if item.type == "branch" { item.condition } else { item.title }
    let body = stack(dir: ttb, spacing: if boxed { t.branch-gap } else { t.row-gap },
      if boxed { align(center, text(weight: 700, title)) } else {
        // Optically center the capital letters within the padded line box.
        pad(y: t.condition-margin,
          move(dy: 0.2 * t.note-size, note(title, inner, t, emphatic: true)))
      },
      stack(dir: ttb, spacing: t.row-gap, ..item.blocks.map(child => render-block(child, inner, t))),
    )
    pad(y: if boxed { t.box-margin } else { 0pt },
      block(width: width, breakable: false,
      inset: if boxed { t.inset } else { 0pt },
      stroke: if boxed { t.outline } else { none }, body))
  } else {
    panic("Unknown block type: " + item.type)
  }
}

#let render-blocks(items, width, t) = stack(dir: ttb, spacing: t.row-gap,
  ..items.map(item => render-block(item, width, t)))

#let section(procedure, width, t) = context {
  assert(("normal", "emergency").contains(procedure.category), message: "Unknown section category")
  let emergency = procedure.category == "emergency"
  let title = text(font: t.header-font, size: t.header-size, weight: 700,
    tracking: t.header-tracking, fill: if emergency { white } else { black },
    procedure.title)
  let title-width = width - 2 * t.inset
  for word in procedure.title.split(regex("\\s+")) {
    assert(measure(text(font: t.header-font, size: t.header-size, weight: 700,
      tracking: t.header-tracking, word)).width <= title-width,
      message: "Unbreakable word in section title: " + word)
  }
  let title-body = block(width: title-width, align(center, title))
  let heading-height = calc.max(t.header-height, measure(title-body).height + 2 * t.inset)
  let heading = block(width: width, height: heading-height, breakable: false,
    fill: if emergency { t.emergency-fill } else { t.normal-fill },
    stroke: (top: t.rule),
    align(center + horizon, title-body),
  )
  stack(dir: ttb, spacing: t.heading-gap,
    heading,
    pad(x: t.inset, render-blocks(procedure.blocks, width - 2 * t.inset, t)),
  )
}

#let fit-region(body, width, height, name) = context {
  // Measure natural content at its real width, BEFORE imposing region height.
  let actual = measure(body, width: width)
  assert(actual.height <= height + 0.05pt,
    message: "Layout overflow in " + name + ": needs " + repr(actual.height)
      + ", available " + repr(height))
  assert(actual.width <= width + 0.05pt, message: "Width overflow in " + name)
  block(width: width, height: height, breakable: false, body)
}

#let procedure-column(ids, procedures, width, height, name, t, stretch-min-fill: none) = context {
  let render(scale) = {
    let spaced = t
    // Only vertical whitespace changes: fonts, widths, and box insets stay fixed.
    for key in ("row-gap", "note-gap", "section-gap", "box-margin", "condition-margin", "line-leading",
      "note-leading", "response-gap", "branch-gap", "heading-gap") {
      spaced.insert(key, t.at(key) * scale)
    }
    set par(leading: spaced.line-leading)
    stack(dir: ttb, spacing: spaced.section-gap,
      ..ids.map(id => {
        assert(procedures.keys().contains(id), message: "Unknown procedure: " + id)
        section(procedures.at(id), width, spaced)
      }))
  }
  let content = render(1)
  if stretch-min-fill != none {
    assert(stretch-min-fill > 0 and stretch-min-fill <= 1,
      message: "Stretch minimum fill must be in (0, 1]")
    let natural = measure(content, width: width).height
    if natural >= height * stretch-min-fill and natural < height {
      // With fixed widths/type, height is linear in these spacing lengths.
      let growth = measure(render(2), width: width).height - natural
      if growth > 0pt {
        content = render(calc.min(2, 1 + (height - natural) / growth))
      }
    }
  }
  fit-region(content, width, height, name + " [" + ids.join(", ") + "]")
}

#let validate-procedures(procedures) = {
  let seen = ()
  let walk(items) = {
    let ids = ()
    for item in items {
      assert(item.keys().contains("id"), message: "Every block needs a stable id")
      ids.push(item.id)
      if item.type == "check" {
        assert(type(item.challenge) == str, message: "Challenge must be a quoted string: " + item.id)
        assert(type(item.response) == str, message: "Response must be a quoted string: " + item.id)
      }
      if item.keys().contains("blocks") { ids += walk(item.blocks) }
    }
    ids
  }
  for (id, procedure) in procedures {
    let ids = walk(procedure.blocks)
    for block-id in ids {
      assert(not seen.contains(block-id), message: "Duplicate block id: " + block-id)
      seen.push(block-id)
    }
  }
}
