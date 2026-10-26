"""Refresh data/scholar.json from Google Scholar.

Run by .github/workflows/update-scholar.yml (or locally: pip install scholarly && python scripts/update_scholar.py).
Google Scholar sometimes blocks automated requests. If that happens this script
leaves the existing file untouched and exits cleanly, so the site keeps its last good numbers.
"""
import json, sys, datetime, pathlib

SCHOLAR_ID = "2IIG2FcAAAAJ"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "scholar.json"

try:
    from scholarly import scholarly
    author = scholarly.fill(scholarly.search_author_id(SCHOLAR_ID), sections=["indices"])
    data = {
        "citations": int(author.get("citedby", 0)),
        "h_index": int(author.get("hindex", 0)),
        "i10_index": int(author.get("i10index", 0)),
        "updated": datetime.date.today().isoformat(),
        "profile": f"https://scholar.google.com/citations?user={SCHOLAR_ID}",
    }
except Exception as exc:  # blocked, captcha, network, parsing
    print(f"Scholar fetch failed, keeping existing file: {exc}")
    sys.exit(0)

old = json.loads(OUT.read_text()) if OUT.exists() else {}
if {k: old.get(k) for k in ("citations", "h_index", "i10_index")} == {k: data[k] for k in ("citations", "h_index", "i10_index")}:
    print("No change in metrics.")
    sys.exit(0)
OUT.write_text(json.dumps(data, indent=2) + "\n")
print("Updated:", data)
