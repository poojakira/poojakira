# Setup — AI Security Assistant (scanner chatbot)

This folder is a **self-contained, static website**. No backend, no API keys, no build step, no cost.
It runs a client-side assistant that greets visitors and answers questions about you, using your photo
as an animated "biometric scanner" avatar.

```
ai-assistant-site/
├─ index.html      ← page + scanner UI
├─ styles.css      ← scanner / cyber theme
├─ knowledge.js    ← ALL the facts the bot answers from (edit this to update answers)
├─ app.js          ← boot sequence, greeting, typing, intent matching
└─ photo.jpg       ← YOUR photo (you add this — see step 1)
```

---

## 1. Add your photo

Drop a square-ish headshot into this folder named **`photo.jpg`**.

- Recommended: square crop, at least 400×400 px.
- If you don't add one, the site automatically falls back to your GitHub avatar
  (`avatars.githubusercontent.com/u/90021441`), so it still works — but a real photo looks best.
- Prefer a different filename/format? Change the `src="photo.jpg"` line in `index.html`.

---

## 2. Test it locally (optional but recommended)

Because it's pure static files, just open `index.html` in a browser — or serve it:

```bash
# from inside the ai-assistant-site folder
python -m http.server 8000
# then visit http://localhost:8000
```

You should see: a boot sequence → the scanner scanning your photo → a greeting → clickable
question chips. Type a question or click a chip.

---

## 3. Deploy to GitHub Pages

### Option A — dedicated repo (matches the README button URL)

The README button points to `https://poojakira.github.io/ai-assistant-site/`, which expects a repo
named **`ai-assistant-site`**.

```bash
# create the repo on GitHub first (name it: ai-assistant-site), then:
cd ai-assistant-site
git init
git add .
git commit -m "AI Security Assistant scanner bot"
git branch -M main
git remote add origin https://github.com/poojakira/ai-assistant-site.git
git push -u origin main
```

Then on GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch →
Branch: `main` / `root` → Save.**
Wait ~1 minute; your site goes live at `https://poojakira.github.io/ai-assistant-site/`.

### Option B — put it inside your profile repo

If you'd rather host it under your existing `poojakira/poojakira` repo, copy this folder there,
enable Pages the same way, and update the README button URL to
`https://poojakira.github.io/ai-assistant-site/` (path stays the same if the folder name matches).

---

## 4. Update the README button (only if your URL differs)

In `README.md`, the launch button is:

```html
<a href="https://poojakira.github.io/ai-assistant-site/">
```

Change that URL if you deployed to a different repo/path.

---

## 5. Keep the bot's answers accurate

Everything the bot "knows" lives in **`knowledge.js`**:

- `KB.greetings` — the hello messages.
- `KB.intents[]` — each has `keywords` (what triggers it) and an `answer` (HTML allowed).
- `KB.fallback` — shown when nothing matches.

To add a new topic, copy an existing intent block, give it an `id`, add trigger `keywords`,
and write the `answer`. To change a fact (e.g., graduation date, new project), just edit the text.

The matcher scores multi-word phrases highest, then exact words, then singular/plural variants —
so add a few natural phrasings a visitor might type.

---

## Notes / honest limitations

- This is a **rule-based assistant**, not an LLM. It answers well on the topics in `knowledge.js`
  and gives a helpful fallback otherwise. That's intentional: it's free, private, has no API keys
  to leak, and can't hallucinate facts about you — fitting for a security engineer's portfolio.
- Want a true LLM-backed version later? You'd add a serverless endpoint (e.g., a small proxy to an
  LLM API) and call it from `app.js`. Not required for this to work.
