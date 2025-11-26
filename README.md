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

### Prerequisites

Before deploying your site, ensure the following setup is complete:

1. **Cloudflare Account**: You need a Cloudflare account with access to Workers and Pages. If you don't have one, sign up at [cloudflare.com](https://cloudflare.com).

2. **Install Cloudflare Workers and Pages App**: In GitHub, go to the [Cloudflare Workers and Pages app](https://github.com/apps/cloudflare-workers-and-pages) in the GitHub Marketplace and install it for your account or organization. Grant access to the repositories you want to deploy from.

3. **GitHub Repository Access**: In GitHub, go to Profile > Settings > Integrations > Applications > Cloudflare Workers and Pages > Configure > Repository access, and grant access to your repository.

4. **Create Cloudflare Pages Project**: In the Cloudflare dashboard, navigate to Workers & Pages > Create Application > Pages tab > Connect to Git. Select your GitHub repository from the list.

5. **Build Settings Verification**: After running `stw init`, confirm that the project name and build path in Cloudflare Pages' advanced settings match the values in your updated `wrangler.json` file.

### Deployment Steps

Follow these steps to deploy your site:

1. **Initialize Configuration**: Run `stw init` in your terminal. This command will prompt you to enter a project name (default: stw-site) and a custom domain (e.g., yoursite.com). It will update the `wrangler.json` file with these values.

2. **Build the Site**: Execute `stw build` to generate the static files. This will create or update the `dist/` directory with your built website.

3. **Commit the Build Output**: Add the `dist/` directory and the updated `wrangler.json` file to your Git repository by running:
   ```bash
   git add dist/ wrangler.json
   git commit -m "Add built site and deployment config"
   ```
   Push this commit to your repository.

4. **Merge to Main Branch**: Create a pull request or merge your changes into the `main` branch. Cloudflare Pages will automatically detect the changes and deploy your site based on the configured build settings.

## Customization

- Edit `templates/base.html` for layout.
- Add more pages in `pages/`.
- Modify CSS in `assets/css/style.css`.
- Add JS in `assets/js/app.js`.