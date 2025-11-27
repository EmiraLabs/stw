# STW - Static Website Template

This is a GitHub template for building static websites deployable to Cloudflare using the STW CLI.

## Features

- **SEO Meta Support**: Per-page and site-wide SEO metadata with front matter
- Go template-based rendering
- YAML configuration
- Nested page routing
- Live reload in development
- Cloudflare Pages deployment
- Minimal, fast static generation

## Installation

1. Click "Use this template" on GitHub to create a new repository.
2. Clone your new repository: `git clone https://github.com/yourusername/yourrepo.git`
3. Install the STW CLI: `go install github.com/EmiraLabs/stw-cli@latest`

## How it works

- `pages/`: Contains your page content as HTML snippets.
- `templates/`: Base HTML template with placeholders like `{{content}}` and `{{title}}`.
- `assets/`: CSS, JS, images, etc.

## Deploy the Site

To deploy your site to Cloudflare Pages:

1. Run `stw init` to configure project name and domain.
2. Build with `stw build`.
3. Commit and push to GitHub; Cloudflare Pages will auto-deploy.

For detailed instructions, including prerequisites and setup, see [docs/deployment.md](docs/deployment.md).

## Customization

- [Templates](docs/templating.md): Edit `templates/base.html` for layout.
- [Pages](docs/pages.md): Add more pages in `pages/`.
- [Assets](docs/assets.md): Modify CSS in `assets/css/style.css` and add JS in `assets/js/app.js`.
- [Configuration](docs/config.md): Edit `config.yaml` for navigation and content.

## Documentation

See [docs/README.md](docs/README.md) for detailed documentation.