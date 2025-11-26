# Templating

The STW CLI uses Go templates for rendering HTML pages. Templates are stored in the `templates/` directory and use the `.html` extension.

## Base Template

The main template is `templates/base.html`, which provides the overall HTML structure.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minimal Site</title>
    <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
    {{template "header.html" .}}
    <main>
        {{.Content}}
    </main>
    {{template "footer.html" .}}
    <script src="/assets/js/app.js"></script>
    <!-- Development reload script -->
    {{if .IsDev}}
    <script>
        // EventSource for live reload in development
    </script>
    {{end}}
</body>
</html>
```

Key elements:
- `{{template "header.html" .}}`: Includes the header component
- `{{.Content}}`: Placeholder for page-specific content
- `{{template "footer.html" .}}`: Includes the footer component
- `{{if .IsDev}}`: Conditional block for development features

## Components

Reusable template components are stored in `templates/components/`.

### Header (`templates/components/header.html`)

```html
<header>
    <div>
        <h1>
            <a href="/">Minimal Site</a>
        </h1>
        <nav>
            {{ range .Config.navigations }}
            <a href="{{.url}}">{{.name}}</a>
            {{ end }}
        </nav>
    </div>
</header>
```

Uses `{{ range .Config.navigations }}` to loop through navigation items from `config.yaml`.

### Footer (`templates/components/footer.html`)

```html
<footer>
    <div>
        <p>&copy; 2025 My Minimal Site. All rights reserved.</p>
    </div>
</footer>
```

Simple footer component.

## Template Syntax

STW uses Go's template syntax:
- `{{.Variable}}`: Access variables
- `{{range .Array}} ... {{end}}`: Loop over arrays
- `{{if .Condition}} ... {{end}}`: Conditional rendering
- `{{template "name.html" .}}`: Include other templates

## Page Rendering

Each page in `pages/` is rendered using `base.html` as the layout, with the page content inserted at `{{.Content}}`.