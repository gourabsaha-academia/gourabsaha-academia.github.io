# Gourab Saha · Academic Portfolio

Static academic website (HTML + Tailwind CSS via CDN + vanilla JS). No build step. Free hosting on GitHub Pages.

## Folder structure

```
gourab-saha.github.io/            ← repository root
├── index.html                    ← the whole site (HTML, styles, scripts)
├── .nojekyll                     ← tells GitHub Pages to serve files as-is
├── README.md
├── assets/
│   ├── profile.jpg               ← hero photo (4:5 portrait works best)
│   ├── Gourab_Saha_CV.pdf        ← PUBLIC CV: no phone, referees or IELTS
│   └── posters/
│       ├── paper1.png            ← AWH review (Applied Thermal Engineering 2026)
│       ├── paper2.png            ← Solar PV refrigeration review (Energy Reports 2024)
│       ├── paper3.png            ← IoT precision agriculture (PLOS ONE 2025)
│       └── thumbs/
│           ├── paper1.webp       ← small previews used on the cards (720×900)
│           ├── paper2.webp
│           └── paper3.webp
├── data/
│   └── scholar.json              ← citations / h-index / i10-index shown on the site
├── scripts/
│   └── update_scholar.py         ← used by the optional GitHub Action
└── .github/
    └── workflows/
        └── update-scholar.yml    ← optional weekly Scholar refresh
```

## Deploy on GitHub Pages

**Step 1: Create the repository**
1. Sign in at github.com → **New repository**.
2. For the address `https://<username>.github.io`, name the repo exactly `<username>.github.io`.
   Any other name (e.g. `portfolio`) works too and is served at `https://<username>.github.io/portfolio/`.
3. Set it to **Public**. Don't add a README; this folder already has one.

**Step 2: Upload the files**

*Web UI:* open the empty repo → **uploading an existing file** → drag in the *contents* of this folder (not the folder itself), including `assets/`, `data/`, `scripts/`, `.github/` and `.nojekyll` → **Commit changes**.
Hidden files: on macOS press `Cmd+Shift+.` in Finder to see `.nojekyll` and `.github`. If the browser upload skips `.github`, the site still works; only the auto-refresh Action is missing.

*Git CLI:*
```bash
cd path/to/this/folder
git init
git add .
git commit -m "Initial portfolio"
git branch -M main
git remote add origin https://github.com/<username>/<username>.github.io.git
git push -u origin main
```

**Step 3: Turn on Pages**
Repo → **Settings** → **Pages** → *Build and deployment* → Source: **Deploy from a branch** → Branch: **main**, folder **/ (root)** → **Save**.

**Step 4: Check the live site**
After 1–2 minutes, the Pages settings screen shows *"Your site is live at …"*. Open it and check that:
- the photo and the three poster thumbnails load, and clicking a poster opens the lightbox,
- **CV (PDF)** opens the public CV,
- the Scholar card shows your numbers (see below).
Changes you push later go live within about a minute. Hard-refresh (`Ctrl+Shift+R`) if you still see the old version.

## Google Scholar metrics

Google Scholar has no public API and blocks browser requests, so the site reads `data/scholar.json` (example values shown):

```json
{ "citations": 42, "h_index": 3, "i10_index": 1, "updated": "2026-10-25" }
```

- **Manual (reliable):** copy the three numbers from your Scholar profile into this file and commit. Until you do, the card shows "—" and links to Scholar.
- **Automatic (optional):** the Action in `.github/workflows/update-scholar.yml` runs every Monday (or on demand from the **Actions** tab → *Run workflow*). If Scholar blocks it, the file is left as it was, so the site never breaks.

## Adding a new paper

- **Journal article:** copy one `<article class="pub ... data-type="journal"">` block in `index.html`, then update the title, authors (wrap your name in `<span class="me">G. Saha</span>`), venue, DOI and summary. Put the poster in `assets/posters/paper4.png` with a 720×900 preview in `assets/posters/thumbs/paper4.webp`. If you skip the .webp, the card falls back to the .png.
- **Conference paper:** copy a block with `data-type="conference"`.
- `data-topic` controls the topic filter. Use one or more of `energy agri ai bio`.
- The filter counts update automatically.

## Privacy

The public CV in `assets/` was redacted from the full CV: phone number, references and IELTS details are removed from the page and from the PDF's text layer. Keep the full CV out of this repository; anything pushed to a public repo stays in its history.
