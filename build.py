#!/usr/bin/env python3
import os
import shutil
import argparse
from pathlib import Path

# Simple static site generator
# No dependencies, just Python standard library

def configure_wrangler(name, domain):
    wrangler_file = Path('wrangler.json')
    if wrangler_file.exists():
        content = wrangler_file.read_text()
        content = content.replace('{{ project_name}}', name)
        content = content.replace('{{ domain }}', domain)
        wrangler_file.write_text(content)
        print(f"Configured wrangler.json with name: {name}, domain: {domain}")

def build_site():
    src_dir = Path('src')
    templates_dir = Path('templates')
    static_dir = Path('static')
    dist_dir = Path('dist')

    # Clear dist
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    dist_dir.mkdir()

    # Copy static files
    if static_dir.exists():
        shutil.copytree(static_dir, dist_dir / 'static')

    # Load base template
    base_template = (templates_dir / 'base.html').read_text()

    # Process pages
    for page_file in src_dir.glob('*.html'):
        content = page_file.read_text()
        html = base_template.replace('{{content}}', content)
        output_file = dist_dir / page_file.name
        output_file.write_text(html)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build the static site and configure Wrangler.')
    parser.add_argument('--name', required=True, help='Project name for Wrangler')
    parser.add_argument('--domain', required=True, help='Custom domain for Wrangler')
    args = parser.parse_args()

    configure_wrangler(args.name, args.domain)
    build_site()
    print("Site built successfully!")