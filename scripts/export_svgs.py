"""Writes every shown asset to dist/svg as a flat-hex SVG (default brand colour).
Usage: python3 scripts/export_svgs.py"""
import pathlib
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
out = ROOT / "public" / "dist" / "svg"; out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto((ROOT / "public" / "index.html").as_uri()); pg.wait_for_timeout(600)
    files = pg.evaluate("()=>{S.mode='flat';return ASSETS.filter(a=>!a.hidden).map(a=>[a.id,svgFile(a,512)])}")
    b.close()
for id_, svg in files:
    (out / f"{id_}.svg").write_text(svg)
print(f"wrote {len(files)} files to {out}")
