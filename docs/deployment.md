# Deployment

The site is deployed to Cloudflare Pages via GitHub integration. Configuration is stored in `wrangler.json`.

## Prerequisites

Before deploying your site, ensure the following setup is complete:

1. **Cloudflare Account**: You need a Cloudflare account with access to Workers and Pages. If you don't have one, sign up at [cloudflare.com](https://cloudflare.com).

2. **Install Cloudflare Workers and Pages App**: In GitHub, go to the [Cloudflare Workers and Pages app](https://github.com/apps/cloudflare-workers-and-pages) in the GitHub Marketplace and install it for your account or organization. Grant access to the repositories you want to deploy from.

3. **GitHub Repository Access**: In GitHub, go to Profile > Settings > Integrations > Applications > Cloudflare Workers and Pages > Configure > Repository access, and grant access to your repository.

4. **Create Cloudflare Pages Project**: In the Cloudflare dashboard, navigate to Workers & Pages > Create Application > Pages tab > Connect to Git. Select your GitHub repository from the list.

5. **Build Settings Verification**: After running `stw init`, confirm that the project name and build path in Cloudflare Pages' advanced settings match the values in your updated `wrangler.json` file.

## Deployment Steps

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

## Wrangler Configuration

```json
{
  "name": "{{ .project_name}}",
  "compatibility_date": "2025-11-17",
  "assets": {
    "directory": "./dist"
  },
  "routes": [
    {
      "pattern": "{{ .domain }}",
      "custom_domain": true
    }
  ]
}
```

### Fields

- `name`: Project name (set during `stw init`)
- `compatibility_date`: Cloudflare compatibility date
- `assets.directory`: Directory containing built static files (`./dist`)
- `routes`: Custom domain routing configuration

## Setup

Run `stw init` to configure deployment:
- Prompts for project name and custom domain
- Generates `wrangler.json` with your settings