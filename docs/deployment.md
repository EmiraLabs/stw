# Deployment

The site is deployed to Cloudflare using Wrangler. Configuration is stored in `wrangler.json`.

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

## Prerequisites

- Cloudflare account with Workers and Pages access
- Custom domain configured in Cloudflare
- Wrangler CLI installed (`npm install -g wrangler`)

## Deploying

After building with `stw build`, deploy using:

```bash
wrangler deploy
```

Or use the STW CLI deployment command if available.

## Custom Domain

The `routes` section configures the custom domain. Ensure your domain is set up in Cloudflare DNS and SSL/TLS settings.