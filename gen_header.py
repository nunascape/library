"""Library header. Generated into every page by build.py — edit here, not in public/.

Active tab: build.py stamps data-section on <html>; style.css lights the
matching [data-tab]. No JavaScript.
Theme: the solid nuna tile above LIBRARY is a <label> for the #paper
checkbox, so it flips black/newsprint with no JavaScript either.
"""
import core

# no Home tab — the LIBRARY wordmark is the way home
TABS = [("Paint", "/paint", "paint"), ("Games", "/games", "games"),
        ("Shapes", "/shapes", "shapes"), ("Patterns", "/patterns", "patterns")]
SECTIONS = {key for _, _, key in TABS}
SURFACE = "https://nunascape.com"

# the pastel spectrum of the surface site, carried on one tile
PRISM = ["#F2657A", "#F5B342", "#EDE45C", "#8FD46A", "#58C6C0", "#63A7E8", "#9D7FD4"]


def section_of(path: str) -> str:
    """Which tab a URL lights. Books and the index light Home."""
    seg = path.strip("/").split("/", 1)[0]
    if seg in SECTIONS:
        return seg
    return "home"   # the index and the books light no tab


def _tile(cls: str, fill: str, extra: str = "") -> str:
    return (f'<svg class="{cls}" viewBox="-104 -104 208 320" aria-hidden="true">'
            f'<path d="{core.TILE}" fill="{fill}"{extra}></path></svg>')


def header_html() -> str:
    tabs = "".join(
        f'<a class="nh-tab" href="{href}" data-tab="{key}">{name}</a>'
        for name, href, key in TABS)
    stops = "".join(
        f'<stop offset="{i / (len(PRISM) - 1):.3f}" stop-color="{c}"></stop>'
        for i, c in enumerate(PRISM))
    prism = ('<svg class="nh-prism" viewBox="-104 -104 208 320" aria-hidden="true">'
             '<defs><linearGradient id="nhPrism" x1="0" y1="0" x2="1" y2="1">'
             f'{stops}</linearGradient></defs>'
             f'<path d="{core.TILE}" fill="url(#nhPrism)"></path></svg>')
    return f'''<header id="nuna-nav">
  <div class="nh-mast">
    <label class="nh-switch" for="paper" title="Black or newsprint">
      {_tile("nh-tile", "currentColor")}
      <span class="nh-sr">Switch between black and newsprint</span>
    </label>
    <a class="nh-word" href="/">LIBRARY</a>
  </div>
  <div class="nh-bar">
    <nav class="nh-tabs" aria-label="Library">{tabs}<a class="nh-out" href="{SURFACE}" title="nunascape.com"><span class="nh-sr">nunascape.com</span>{prism}</a></nav>
  </div>
</header>'''
