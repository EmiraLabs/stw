# Minimal Static Site Generator

This is a very minimal framework for building static websites deployable to Cloudflare Pages.

## How it works

- `pages/`: Contains your page content as HTML snippets.
- `templates/`: Base HTML template with placeholders like `{{content}}` and `{{title}}`.
- `assets/`: CSS, JS, images, etc.
- `main.go`: Go script to generate and serve the site.

## Building the site

Run: `go run main.go --build`

This generates static files in `dist/`.

## Serving locally

Run: `go run main.go --serve`

This builds the site and serves it on http://localhost:8001.

## Deploying to Cloudflare

1. Install Wrangler: `npm install -g wrangler`
2. Authenticate: `wrangler auth login`
3. Build and deploy: `go run main.go --build && wrangler deploy`

This deploys the static site as a Cloudflare Worker with custom domain routing.

## Customization

- Edit `templates/base.html` for layout.
- Add more pages in `pages/`.
- Modify CSS in `assets/css/style.css`.
- Add JS in `assets/js/app.js`.