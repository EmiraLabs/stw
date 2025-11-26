# Configuration

The `config.yaml` file contains site-wide configuration data used by the STW CLI to generate the static site. It uses YAML format and is loaded into the templates as `.Config`.

## Structure

### Navigations

An array of navigation items for the site menu.

```yaml
navigations:
  - name: Home
    url: /
  - name: About
    url: /about/
  - name: Contact
    url: /about/contact/
```

Each item has:
- `name`: The display name for the link
- `url`: The relative URL path

This is used in `templates/components/header.html` to generate the navigation menu.

### Home

Contains content sections for the home page.

```yaml
home:
  contents:
    - title: "<h1>Heading 1</h1>"
      content: "Lorem ipsum..."
    - title: "<h2>Heading 2</h2>"
      content: "Lorem ipsum..."
```

Each content item has:
- `title`: HTML string for the section title
- `content`: Text content for the section

This is used in `pages/index.html` to render the home page content.

## Usage

The config data is accessible in templates as `.Config.navigations` and `.Config.home.contents`. Modify this file to change site navigation and home page content.