# nunascape-library

Source for **library.nunascape.com**. Static site, built by one Python script,
deployed by Cloudflare Pages on every push to `main`.

    python3 _src/build.py
    cd public && python3 -m http.server 8000

- `static/style.css` — the one stylesheet. Tokens, header, index, book pages.
- `_src/gen_header.py` — the header (tabs: Home, Paint, Games, Shapes, Patterns; White | Black).
- `_src/gen_index.py` — Library Home, generated from `books.py`. Never hand-edited.
- `_templates/` — page shell, footer, and `book.html` (the six-slot skeleton to copy).
- `content/` — every other page. Names starting with `_` are skipped.
- `public/` — build output. Never edited, never committed.

**New book page:** copy `_templates/book.html` to `content/book-a.html` (mark code, lower case),
fill the slots, push. It lights the Home tab automatically.

**Active tab, no JavaScript:** `build.py` stamps `data-section` on `<html>`; `style.css` lights the tab.
**White | Black, no JavaScript:** a checkbox sits first in `<body>`; the header's label flips it.
A four-line script only *remembers* the choice between pages.
