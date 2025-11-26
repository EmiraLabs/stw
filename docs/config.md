# Configuration

The `config.yaml` file contains site-wide configuration data used by the STW CLI to generate the static site. It uses YAML format and is loaded into the templates as `.Config`. The configuration is fully flexible, allowing you to define any data structure that suits your site's needs.

## Examples

The following are examples of common configurations. You can define any YAML structure in `config.yaml`, and access it in templates via `.Config`.

### Navigation Menu

For example, you can define an array of navigation items for the site menu:

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

### Home Page Content

For example, you can define content sections for the home page:

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

The config data is accessible in templates as `.Config.navigations` and `.Config.home.contents`. Since the configuration is fully dynamic, any data defined in `config.yaml` can be rendered in templates, including HTML content through Go HTML templates. Modify this file to customize your site's configuration.