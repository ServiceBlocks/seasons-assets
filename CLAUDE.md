# Notes for Claude Code

- Single-file app (`public/index.html`). Keep it that way unless asked to split.
- After any asset change run `python3 scripts/qa.py` and look at the asset rendered large (500px) before committing.
- Fix visual feedback per asset; do not restyle the whole set.
- Keep the shared style: layered colour, top-left light, soft shadow, no thick outlines.
- Always use colour roles through `g.f` / `g.s`, never raw hex inside assets (except via `g.pal`).
- Avoid duplicate attributes on one element (see README).
- Hidden assets (`hidden:true`) are intentionally excluded; do not unhide without being asked.
- Owner prefers short, conversational replies.
