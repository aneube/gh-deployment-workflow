#!/usr/bin/env python3
"""
Script to dynamically generate index.html
"""

from datetime import datetime


def generate_html():
    """Generate the index.html file dynamically"""
    
    # Get current timestamp
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Actions Deployment</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #333;
        }}
        
        .container {{
            background: white;
            border-radius: 20px;
            padding: 3rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            text-align: center;
            max-width: 600px;
            width: 90%;
        }}
        
        h1 {{
            color: #667eea;
            margin-bottom: 1rem;
            font-size: 2.5rem;
        }}
        
        p {{
            color: #666;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            line-height: 1.6;
        }}
        
        .timestamp {{
            background: #f5f5f5;
            padding: 1rem;
            border-radius: 10px;
            margin-top: 2rem;
            font-family: 'Courier New', monospace;
            color: #333;
        }}
        
        .emoji {{
            font-size: 4rem;
            margin-bottom: 1rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="emoji">🚀</div>
        <h1>Hello, GitHub Actions!</h1>
        <p>This page was dynamically generated using Python.</p>
        <p>Your deployment workflow is working perfectly!</p>
        <div class="timestamp">
            Generated at: {current_time}
        </div>
    </div>
</body>
</html>
"""
    
    # Write to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Successfully generated index.html at {current_time}")


if __name__ == "__main__":
    generate_html()

