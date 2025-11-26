# STW - Static Website Template

This is a GitHub template for building static websites deployable to Cloudflare using the STW CLI.

## Installation

1. Click "Use this template" on GitHub to create a new repository.
2. Clone your new repository: `git clone https://github.com/yourusername/yourrepo.git`
3. Install the STW CLI: `go install github.com/EmiraLabs/stw-cli@latest`

## How it works

- `pages/`: Contains your page content as HTML snippets.
- `templates/`: Base HTML template with placeholders like `{{content}}` and `{{title}}`.
- `assets/`: CSS, JS, images, etc.

## Building the site

Run: `stw build`

This generates static files in `dist/`.

## Serving locally

Run: `stw serve`

This builds the site and serves it on http://localhost:8080.

## Initialize Deployment Configuration

To set up deployment configuration:

```bash
stw init
```

This will prompt you for:
- **Project name** (default: stw-site)
- **Custom domain** (required, e.g., yoursite.com)

It creates a `wrangler.json` file with your specified values, configured for Cloudflare Workers deployment with static assets.

## Deploy the Site

To deploy your site to Cloudflare Pages:

1. Run `stw init` to configure project name and domain.
2. Build with `stw build`.
3. Commit and push to GitHub; Cloudflare Pages will auto-deploy.

For detailed instructions, including prerequisites and setup, see [docs/deployment.md](docs/deployment.md).

## Customization

- Edit `templates/base.html` for layout.
- Add more pages in `pages/`.
- Modify CSS in `assets/css/style.css`.
- Add JS in `assets/js/app.js`.

## Documentation

See [docs/README.md](docs/README.md) for detailed documentation.