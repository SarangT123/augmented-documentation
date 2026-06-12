# augmented-documentation

Static documentation site hosted on GitHub Pages.

## Structure
- `build.py` — Generates `website/static/index.html` by scanning the docs directories
- `website/static/` — Static site content (deployed to Pages)
- `.github/workflows/deploy.yml` — GitHub Actions workflow for automated deployment

## Local development
```bash
python build.py
python -m http.server 8000 -d website/static
```

## Deployment
Push to `main` — the GitHub Actions workflow automatically builds and deploys to Pages.

To enable: go to repo **Settings → Pages → Source: GitHub Actions**.
