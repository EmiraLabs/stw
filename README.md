# ✨ STW - Static Website Template

[![Go Version](https://img.shields.io/badge/go-%3E%3D1.19-blue)](https://golang.org/)

> A powerful, minimal static site generator for building fast, SEO-friendly websites deployable to Cloudflare Pages.

STW (Static Website Template) is a GitHub template that combines the simplicity of static sites with the power of Go templating, making it easy to create and deploy beautiful websites quickly.

## Features

- **SEO Optimized**: Built-in SEO meta support with front matter for per-page and site-wide metadata
- **Fast Generation**: Minimal, lightning-fast static site generation using Go templates
- **Cloudflare Ready**: Seamless deployment to Cloudflare Pages with zero configuration
- **Live Reload**: Hot reloading during development for instant feedback
- **Responsive**: Mobile-first design with customizable CSS and JS
- **Nested Routing**: Support for nested page structures and clean URLs
- **YAML Config**: Simple configuration with YAML for navigation, content, and settings

## Quick Start

### 1. Use This Template

Click the **"Use this template"** button on GitHub to create your own repository.

### 2. Clone & Install

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
go install github.com/EmiraLabs/stw-cli@latest
```

### 3. Configure & Build

```bash
stw init    # Configure project name and domain
stw serve   # Start development server with live reload
stw build   # Generate static files
```

### 4. Deploy

Push to GitHub and let Cloudflare Pages handle the deployment automatically!

## Project Structure

```
stw/
├── config.yaml          # Site configuration and navigation
├── wrangler.json        # Cloudflare deployment settings
├── pages/               # Your page content (HTML snippets)
│   ├── index.html
│   └── about/
│       └── index.html
├── templates/           # Go HTML templates
│   ├── base.html        # Main layout template
│   ├── components/      # Reusable components
│   └── partials/        # Template partials
├── assets/              # Static assets
│   ├── css/
│   └── js/
└── docs/                # Comprehensive documentation
```

## How It Works

- **Pages**: Write content in `pages/` as simple HTML with front matter for metadata
- **Templates**: Use Go templates in `templates/` for layout and dynamic content
- **Assets**: Add CSS, JS, and images in `assets/` for styling and interactivity
- **Config**: Customize site-wide settings in `config.yaml`

## Documentation

Dive deep into STW with our comprehensive documentation:

- [Configuration](docs/config.md) - Site config, navigation, and data
- [Templating](docs/templating.md) - Go template system guide
- [Pages](docs/pages.md) - Content structure and front matter
- [Assets](docs/assets.md) - Managing static files
- [Building](docs/building.md) - Build and serve commands
- [Deployment](docs/deployment.md) - Cloudflare Pages deployment
- [SEO Meta](docs/seo-meta.md) - Complete SEO configuration guide

## Customization

- **Layout**: Edit `templates/base.html` for your site's structure
- **Styling**: Modify `assets/css/styles.css` for custom designs
- **Scripts**: Add interactivity with `assets/js/app.js`
- **Content**: Create new pages in `pages/` directory

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Built with ❤️ by [EmiraLabs](https://emiralabs.com)**