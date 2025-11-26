#!/usr/bin/env python3
"""
Script to dynamically generate index.html
"""

from datetime import datetime
from pathlib import Path
from string import Template


class CustomTemplate(Template):
    """Custom template class that uses {variable} syntax instead of $variable"""
    delimiter = '{'
    pattern = r'''
    \{(?:
      (?P<escaped>\{) |   # Escape sequence of two delimiters
      (?P<named>[\w]+)\} |  # delimiter and a Python identifier
      (?P<braced>[\w]+)\} |  # delimiter and a braced identifier
      (?P<invalid>)      # Other ill-formed delimiter exprs
    )
    '''


def generate_html(template_file='index_template.md', output_file='index.md'):
    """Generate the index.md file dynamically from a template"""
    
    # Get current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Read template file
    template_path = Path(template_file)
    if not template_path.exists():
        raise FileNotFoundError(f"Template file '{template_file}' not found")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # Use Template class for more Pythonic string substitution
    template = CustomTemplate(template_content)
    html_content = template.safe_substitute(timestamp=current_time)
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Successfully generated {output_file} at {current_time}")


if __name__ == "__main__":
    generate_html()

