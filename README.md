# STW - Static Website

This is a template for building static websites deployable to Cloudflare Pages using the STW CLI.

## Installation

1. Clone this repository: `git clone https://github.com/EmiraLabs/stw.git`
2. Install the STW CLI: `go install github.com/EmiraLabs/stw-cli@latest`

## How it works

- `pages/`: Contains your page content as HTML snippets.
- `templates/`: Base HTML template with placeholders like `{{content}}` and `{{title}}`.
- `assets/`: CSS, JS, images, etc.

## Building the site

Run: `stw --build`

This generates static files in `dist/`.

## Serving locally

Run: `stw --serve`

This builds the site and serves it on http://localhost:8001.

## Deploying to Cloudflare

1. Install Wrangler: `npm install -g wrangler`
2. Authenticate: `wrangler auth login`
3. Build and deploy: `stw --build && wrangler deploy`

This deploys the static site as a Cloudflare Worker with custom domain routing.

## Customization

- Edit `templates/base.html` for layout.
- Add more pages in `pages/`.
- Modify CSS in `assets/css/style.css`.
- Add JS in `assets/js/app.js`.