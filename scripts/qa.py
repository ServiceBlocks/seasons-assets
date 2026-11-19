"""Sanity checks: every shown asset must be valid XML in every export mode.
Usage: python3 scripts/qa.py   (needs: pip install playwright; playwright install chromium)"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto((ROOT / "public" / "index.html").as_uri())
    pg.wait_for_timeout(600)
    bad = pg.evaluate("""()=>{const bad=[];for(const sh of [0,1])for(const tx of [0,1])for(const m of ['flat','vars']){
      S.shadow=!!sh;S.texture=!!tx;S.mode=m;
      for(const a of ASSETS.filter(a=>!a.hidden)){const s=svgFile(a,480);
        const d=new DOMParser().parseFromString(s,'image/svg+xml');
        if(d.querySelector('parsererror')||/NaN|undefined/.test(s))bad.push([sh,tx,m,a.id])}}return bad}""")
    b.close()
print("invalid exports:", json.dumps(bad), "| page errors:", errs)
sys.exit(1 if bad or errs else 0)
