# STW Documentation

STW (Static Website Template) is a Go-based static site generator for building simple websites deployable to Cloudflare.

## Project Structure

```
stw/
├── config.yaml          # Site configuration
├── wrangler.json        # Cloudflare deployment config
├── pages/               # Page content
├── templates/           # HTML templates
├── assets/              # CSS, JS, images
└── docs/                # This documentation
```

## Quick Start

1. Install STW CLI: `go install github.com/EmiraLabs/stw-cli@latest`
2. Run `stw init` to configure deployment
3. Edit `config.yaml` for navigation and content
4. Modify templates in `templates/`
5. Add pages in `pages/`
6. Run `stw serve` to preview locally
7. Run `stw build` to generate static files
8. Deploy with `wrangler deploy`

## Documentation Sections

- [Configuration](config.md) - Site config and data
- [Templating](templating.md) - Go template system
- [Pages](pages.md) - Content structure
- [Assets](assets.md) - Static files
- [Building](building.md) - Build and serve commands
- [Deployment](deployment.md) - Cloudflare deployment
- [SEO Meta System](seo-meta.md) - Complete guide to configuring SEO metadata

## Key Features

- Go template-based rendering
- YAML configuration
- Nested page routing
- Live reload in development
- Cloudflare Pages deployment
- Minimal, fast static generation