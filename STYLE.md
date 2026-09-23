# Library style — current state

These are the choices the Library is using right now and where each one came
from. None of them is a rule. They live as tokens at the top of
`static/style.css`, so changing one changes every page.

## The two sides of the site

nunascape.com (Squarespace) is the light, pastel "dreamscape" front.
library.nunascape.com is the dark "Library floor": academic, technical, with
Escher-like influences. The two are separate sites and share nothing
automatically.

## Colour

| Token | Black | White | Used for |
|---|---|---|---|
| ground | `#060708` | `#F2F4F4` | page background |
| ground-ix | `#08090A` | `#F2F4F4` | header and index background |
| plate | `#0E1214` | `#FFFFFF` | figure panels |
| ink | `#E7EBEC` | `#14181A` | body text |
| bright | `#F4F6F6` | `#14181A` | headings, wordmark |
| soft | `#9AA4A8` | `#556064` | secondary text, labels |
| rule | `#232B2E` | `#CDD4D6` | hairlines |
| pale | `#C9D2D4` | `#14181A` | lead paragraphs, mark codes |
| ac | `#4FB8AE` | `#17837D` | accent |

Current habits: the field stays black and white, and the teal accent marks
something *active*, such as an open shelf, a live status, a focus ring or a lit
tile. Gold and brown are left out.

**Open:** the Starting Kit asks whether light and dark should be two renders
or one that inverts cleanly. Right now it is one set of pages with two token
sets.

## Type

- **Body:** Iowan Old Style → Palatino → Georgia, 17px, line-height 1.62.
- **Labels:** system monospace, 9–11px, uppercase, letterspaced.
- **Wordmark and page titles:** Cormorant Garamond 300. The **a** of *nuna*
  in "nunascape" carries a teal → lavender gradient (`#17837d` → `#7f72cf`).

## Figures

Every figure uses exact arcs, never approximated curves. The tile path and
every combination mark come from `_src/core.py`, and no path is retyped.

## Layout

- No fixed positioning.
- The White/Black switch works without JavaScript.
- Every page prints legibly, and print always comes out on white.

## Header

- **Tabs:** Home · Paint · Games · Shapes · Patterns.
- **Controls:** a White | Black switch, and ↑ surface back to nunascape.com.
- **Background:** a faint nuna tessellation.
- **Active tab:** lit with no JavaScript.

## To settle

- **Book pages:** they light Home and show a breadcrumb. Should they get their
  own tab state instead?
- **Held-open slots:** whether the empty slots stay visible on the index.
