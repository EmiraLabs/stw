# Minimal Static Site Generator

This is a very minimal framework for building static websites deployable to Cloudflare Pages.

## How it works

- `src/`: Contains your page content as HTML snippets.
- `templates/`: Base HTML template with placeholders like `{{content}}` and `{{title}}`.
- `static/`: CSS, JS, images, etc.
- `build.py`: Python script to generate the site into `dist/`.

## Building the site

Run: `python3 build.py --name your_project_name --domain yourdomain.com`

This will configure `wrangler.json` with your project name and domain, then generate static files in `dist/`.

## Deploying to Cloudflare

1. Install Wrangler: `npm install -g wrangler`
2. Authenticate: `wrangler auth login`
3. Build and deploy: `python3 build.py --name your_project_name --domain yourdomain.com && wrangler deploy`

This deploys the static site as a Cloudflare Worker with custom domain routing.

## Customization

- Edit `templates/base.html` for layout.
- Add more pages in `src/`.
- Modify CSS in `static/css/style.css`.
- Add JS in `static/js/app.js`.