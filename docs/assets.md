# Assets

Static assets like CSS, JavaScript, images, and other files are stored in the `assets/` directory. These files are copied to the `dist/` directory during the build process and served from `/assets/` URLs.

## Directory Structure

```
assets/
├── css/
│   └── styles.css
└── js/
    └── app.js
```

## CSS (`assets/css/styles.css`)

Contains the site's stylesheets. The main stylesheet is linked in `templates/base.html`:

```html
<link rel="stylesheet" href="/assets/css/styles.css">
```

The provided `styles.css` includes:
- Modern, clean design with a light background
- Responsive layout
- Typography using system fonts
- Header and navigation styling
- Footer styling

## JavaScript (`assets/js/app.js`)

Contains client-side JavaScript. The main script is loaded in `templates/base.html`:

```html
<script src="/assets/js/app.js"></script>
```

The provided `app.js` includes:
- DOM ready event listener
- Placeholder for additional functionality

## Adding Assets

To add new assets:
1. Place files in appropriate subdirectories under `assets/`
2. Reference them in templates using `/assets/` paths
3. Run `stw build` to copy them to `dist/`

## Images and Other Files

You can add subdirectories for images, fonts, etc.:
- `assets/images/`
- `assets/fonts/`
- `assets/videos/`

Reference them in templates or CSS using `/assets/images/filename.jpg`, etc.