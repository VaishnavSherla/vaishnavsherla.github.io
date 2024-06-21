---
layout: page
title: Projects
permalink: /projects/
---
{% assign project_counter = 1 %}

{% for project in site.projects %}
### {{ project_counter }}. {{ project.name }}

{% if project.image %}
<img class="lazy" data-src="{{ project.image }}" alt="{{ project.name }}">
{% endif %}

- **Description:**
  {% for item in project.description %}
  - {{ item | strip_html }}
  {% endfor %}


{% if project.demo_media %}
{% if project.demo_media_type == "gif" %}
<img class="lazy" data-src="{{ project.demo_media }}" alt="Demo for {{ project.name }}" loading="lazy">
{% elsif project.demo_media_type == "mp4" %}
<video class="lazy" data-src="{{ project.demo_media }}" controls muted loop loading="lazy">
  Your browser does not support the video tag.
</video>
{% endif %}
{% endif %}



- **Links:**
  {% if project.live_link %}
    - **Live:** [{{ project.live_link }}]({{ project.live_link }})
  {% endif %}

  {% if project.github %}
    - **Code:** [{{ project.github }}]({{ project.github }})
  {% endif %}

- **Tech Stack:** {{ project.tech_stack | join: ', ' }}

{% assign project_counter = project_counter | plus: 1 %}

{% endfor %}
