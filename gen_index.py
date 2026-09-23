"""Library Home — a numbered index of what is on the shelves.

Sections are numbered 1..7. Section 1 (Introduction) is held open for
writing that has not been done yet; sections 2..7 carry the book list from
books.py. Combination marks are deliberately not drawn here — the filing
system can be brought back later without touching this file's structure.
"""
import books

# display number, name, standfirst, which books.py shelf feeds it (None = empty)
SECTIONS = [
    (1, "Introduction", "What the Library is, and how to read it.", None),
    (2, "Core Claims", "One atomic, checkable fact per page.", 1),
    (3, "Explorations and Theory", "The work too large to state in a sentence.", 2),
    (4, "Datasets", "Plates and catalogues held whole rather than described.", 3),
    (5, "Models and Tools", "Every model built, in order, including the ones that were replaced.", 4),
    (6, "Physical World", "The shape out in the world, at the scale of a room.", 5),
    (7, "Personal Writing", "", 6),
]

LIVE = ("Built", "Verified", "Compiled")
DIM = ("Open", "Reserved", "Scoped", "Superseded", "Planned", "Speculative", "Shelved")


def index_body() -> str:
    out = []
    for num, name, sub, shelf in SECTIONS:
        bs = [b for b in books.BOOKS if shelf is not None and b[0] == shelf]
        rows = []
        for i, (_, title, blurb, status) in enumerate(bs, start=1):
            live = " is-live" if status in LIVE else ""
            dim = " is-dim" if status in DIM else ""
            rows.append(f'''        <li class="ix-row{dim}">
          <span class="ix-n">{num}.{i}</span>
          <span class="ix-text"><span class="ix-title">{title}</span><span class="ix-blurb">{blurb}</span></span>
          <span class="ix-status{live}">{status}</span>
        </li>''')
        body = ("\n".join(rows) if rows
                else '        <li class="ix-row is-empty"><span class="ix-n"></span>'
                     '<span class="ix-text"><span class="ix-blurb">Nothing filed yet.</span></span>'
                     '<span class="ix-status"></span></li>')
        openattr = " open" if shelf == 1 else ""
        sub_html = f'<p class="ix-sub">{sub}</p>' if sub else ""
        out.append(f'''    <details class="ix-sec"{openattr}>
      <summary>
        <span class="ix-num">{num}</span>
        <span class="ix-name">{name}</span>
        <span class="ix-count">{len(bs)}</span>
        <span class="ix-x" aria-hidden="true"></span>
      </summary>
      {sub_html}
      <ol class="ix-rows">
{body}
      </ol>
    </details>''')

    return '''<!--TITLE: Index-->
<!--LAYOUT: wide-->
<div class="ix-shell">
<div class="ix-wrap">
''' + "\n".join(out) + f'''
  <p class="ix-foot">{len(books.BOOKS)} entries</p>
</div>
</div>'''
