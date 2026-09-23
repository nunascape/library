#!/usr/bin/env python3
"""
library.nunascape.com — site build.

Wraps every page in the shared chrome and writes public/. public/ is
disposable; never edit it. Cloudflare Pages runs this on every push.

    python3 _src/build.py
    cd public && python3 -m http.server 8000

Pages come from two places:
  * generated  — Library Home (gen_index.py). Never hand-edited.
  * content/   — everything else. Files or folders starting with "_" are skipped.

Stamps, replaced in every page:
  <!--PATH-->       the page's own URL             (/book-a)
  <!--SECTION-->    which header tab it lights      (home, paint, games, shapes, patterns)
  <!--TILE-->       the exact upright tile path from core.py
  <!--MARK:ABC-->   the combination mark ABC, drawn by core.symbol()

Page-level comments, read from the first lines of a body:
  <!--TITLE: ...-->   <title>
  <!--LAYOUT: wide--> full-width main (the index); default is the 46rem reading column
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_src"))
import core, gen_header, gen_index  # noqa: E402

SRC, OUT, T = ROOT / "content", ROOT / "public", ROOT / "_templates"

shell  = (T / "page.html").read_text()
footer = (T / "footer.html").read_text()
header = gen_header.header_html()

MARK_RE = re.compile(r"<!--MARK:([A-P]*)-->")


def meta(body: str, key: str, fallback: str = "") -> str:
    for line in body.splitlines()[:6]:
        tag = f"<!--{key}:"
        if tag in line:
            return line.split(tag, 1)[1].split("-->", 1)[0].strip()
    return fallback


def url_of(rel: pathlib.PurePosixPath) -> str:
    path = "/" + rel.with_suffix("").as_posix()
    if path.endswith("/index"):
        path = path[: -len("index")].rstrip("/") or "/"
    return path


def render(rel, body):
    path = url_of(rel)
    body = (MARK_RE.sub(lambda m: core.symbol(m.group(1)), body)
            .replace("<!--TILE-->", core.TILE))
    return (shell
            .replace("<!--HEADER-->", header)
            .replace("<!--BODY-->", body)
            .replace("<!--FOOTER-->", footer)
            .replace("<!--TITLE-->", meta(body, "TITLE", rel.stem))
            .replace("<!--MAINCLASS-->", "is-wide" if meta(body, "LAYOUT") == "wide" else "")
            .replace("<!--SECTION-->", gen_header.section_of(path))
            .replace("<!--PATH-->", path))


def skipped(rel: pathlib.PurePath) -> bool:
    return any(part.startswith("_") for part in rel.parts)


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    pages = {pathlib.PurePosixPath("index.html"): gen_index.index_body()}

    for f in sorted(SRC.rglob("*.html")):
        rel = pathlib.PurePosixPath(f.relative_to(SRC).as_posix())
        if skipped(rel):
            continue
        if rel in pages:
            print(f"error: content/{rel} collides with a generated page", file=sys.stderr)
            return 1
        pages[rel] = f.read_text()

    for rel, body in pages.items():
        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(rel, body))

    # non-HTML files in content/ pass through untouched
    for f in SRC.rglob("*"):
        rel = f.relative_to(SRC)
        if f.is_file() and f.suffix.lower() != ".html" and not skipped(rel):
            dest = OUT / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)

    static = ROOT / "static"
    if static.exists():
        shutil.copytree(static, OUT, dirs_exist_ok=True)

    print(f"built {len(pages)} pages into {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
