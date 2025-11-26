---
layout: default
title: Home
---

# Welcome to My GitHub Page!

This page was generated automatically by **Jekyll** from a Markdown file.

This is my first paragraph of content.

Generated at: {timestamp}

## Recent Posts

{% for post in site.posts %}
  <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
  {% if post.author %}
    <p><small>By {{ post.author }}</small></p>
  {% endif %}
{% endfor %}