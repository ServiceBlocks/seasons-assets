# Seasonal Illustrations

A downloadable seasonal illustration library (Christmas first) for websites and apps. Pick a brand colour, search and filter, select assets, and download transparent SVG or PNG.

The whole app is one file: `public/index.html`. Open it in a browser. No build step.

## Features
- Brand colour picker that re-themes every asset (`brand-accent`, `accent-light`, `accent-dark`); material colours stay fixed.
- Search and category filter, multi-select, size options, PNG or SVG, zip for multiple.
- SVG export as flat hex colours (Figma, Illustrator) or CSS variables (theming in code).
- Toggles for cast shadow and material texture.
- JSZip loads from a CDN for multi-asset downloads.

## Style rules
Mature 2D editorial vector look: layered colour, one consistent top-left light, soft shadows, no thick outlines, no emoji proportions.

## How assets work
Each asset is a function `drawX(g)` returning SVG markup. `g` is made by `makeG(prefix, palette, mode, opts)`:
- `g.f(role)` / `g.s(role, width, extra)` return fill / stroke attributes with `class=role`.
- `g.lg`, `g.rg`, `g.clip`, `g.u`, `g.id` build gradients, clips and unique ids.
- Never put a second `fill`, `class` or `stroke-linecap` on an element that already uses `g.f` / `g.s`: duplicate attributes make the exported SVG invalid XML.

Assets are registered in the `ASSETS` array: `{id, name, cat, tags, draw, hidden?}`. Set `hidden:true` to keep an asset in code but out of the library, the size preview and downloads.

## Status
Shown (19): santa hat, tree, bauble, wreath, gift, candy cane, stocking, bells, candles, snowman, star, mittens, mistletoe, elf hat, snowflake, gingerbread man, cocoa mug, snow globe, hanging ornaments.

Hidden for later (need rework): reindeer, pine branch, penguin, polar bear, holly.

Not built yet: elf character, seamless patterns, other seasons.

## Scripts
```
pip install playwright && playwright install chromium
python3 scripts/qa.py            # validates every asset in every export mode
python3 scripts/export_svgs.py   # writes public/dist/svg/*.svg (default red)
```

## Known gaps
PNG, CSS-variable and zip downloads are verified in headless tests only. Check them once in a real browser after deploying.

## Deploy (Cloudflare Workers)
Static site served via Workers static assets from `public/`.
```
npm install
npm run dev       # local preview
npm run deploy    # wrangler deploy (run `npx wrangler login` first)
```
