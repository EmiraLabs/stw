# Pages

Page content is stored in the `pages/` directory as HTML snippets. Each page corresponds to a route and is rendered using the base template.

## Directory Structure

```
pages/
├── index.html          # Home page (/)
├── about/
│   └── index.html      # About page (/about/)
│   └── contact/
│       └── index.html  # Contact page (/about/contact/)
```

## Page Files

Each `.html` file contains the main content for that page, written as HTML snippets with Go template syntax.

### Home Page (`pages/index.html`)

```html
<section>
    <h1>Welcome to the Home Page</h1>
    <p>This is the home page content.</p>
    {{ range .Config.home.contents }}
    <section>
        {{ .title }}
        <p>{{ .content }}</p>
    </section>
    {{ end }}
</section>
```

This page:
- Displays a welcome message
- Loops through `.Config.home.contents` from `config.yaml` to render dynamic sections

### Nested Pages

Pages can be nested in subdirectories:
- `pages/about/index.html` → `/about/`
- `pages/about/contact/index.html` → `/about/contact/`

## Template Variables

In page templates, you have access to:
- `.Config`: Data from `config.yaml`
- `.Content`: The rendered content (for use in base template)
- `.IsDev`: Boolean indicating development mode

## Adding New Pages

To add a new page:
1. Create an `.html` file in the appropriate location under `pages/`
2. Write the content as HTML with template syntax
3. The URL path matches the file path relative to `pages/`
4. Run `stw build` to generate the static files

## Page Metadata

Currently, pages don't have individual metadata. All pages use the same title and meta tags from `base.html`. For page-specific titles, you could modify the base template to accept title variables.