#!/usr/bin/env python3
"""
Script to dynamically generate index.html
"""

from datetime import datetime
from pathlib import Path


def generate_html(template_file='index_template.md', output_file='index.md'):
    """Generate the index.html file dynamically from a template"""
    
    # Get current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Read template file
    template_path = Path(template_file)
    if not template_path.exists():
        raise FileNotFoundError(f"Template file '{template_file}' not found")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        html_template = f.read()
    
    # Replace placeholder with actual timestamp
    html_content = html_template.replace('{timestamp}', current_time)
    
    # Write to index.html
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Successfully generated {output_file} at {current_time}")


if __name__ == "__main__":
    generate_html()

