---
layout: default
title: Home
---

# Welcome to My GitHub Page!

This page was generated automatically by **Jekyll** from a Markdown file.

This is my first paragraph of content.

Generated at: 2025-11-26 21:30:33


<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>

And this is another way:

{% for post in site.posts %}
  <div class="post-preview">
    <h2>
      <a href="{{ post.url | relative_url }}">
        {{ post.title }}
      </a>
    </h2>
    <p class="post-meta">
      Posted on {{ post.date | date: "%B %d, %Y" }}
    </p>
    {{ post.excerpt }}
    <a href="{{ post.url | relative_url }}">Read More &raquo;</a>
  </div>
{% endfor %}