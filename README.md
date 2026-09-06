# yourstackdoesthat.com

"Your stack does that" is the slogan of the era after apps. This repository is the site and its community-contributed catalog.

- `content/does/` — Does entries, one markdown file each
- `content/ledger/` — Cancel Ledger lines, one markdown file each
- `pages/` — the fixed pages, as HTML bodies with a small front matter block
- `static/` — the stylesheet, robots.txt, favicon
- `build.py` — generates `site/` (Python 3, standard library only)
- `site/` — the generated static site (not committed; Netlify runs `build.py` on deploy)

To contribute, read [CONTRIBUTING.md](CONTRIBUTING.md). To have your stack watch for new entries, see [yourstackdoesthat.com/check-back/](https://yourstackdoesthat.com/check-back/).

Everything here, including the slogan, is released under [CC0 1.0](LICENSE). Nobody owns this phrase.

Maintained by [John Rector](https://johnrector.me/).
