# Building and Serving

The STW CLI handles building and serving the static site.

## Building

To generate static files:

```bash
stw build
```

This:
- Processes templates with page content
- Copies assets to `dist/`
- Generates HTML files in `dist/` matching the `pages/` structure

## Serving Locally

To serve the site locally with live reload:

```bash
stw serve
```

This:
- Builds the site
- Starts a local server on `http://localhost:8080`
- Watches for file changes and rebuilds automatically
- Includes development features like live reload

## Development Workflow

1. Make changes to templates, pages, or config
2. Run `stw serve` to preview locally
3. The site auto-reloads on changes
4. When ready, run `stw build` for production files
5. Deploy the `dist/` directory

## Build Output

The `dist/` directory contains:
- `index.html` and other page HTML files
- `assets/` directory with CSS, JS, images, etc.
- All files ready for static hosting

## CLI Installation

Install the STW CLI:

```bash
go install github.com/EmiraLabs/stw-cli@latest
```

Ensure Go is installed and `$GOPATH/bin` is in your PATH.