---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
tags: []
draft: true
# 1-2 sentences. Becomes the search-result snippet and social preview text.
description: ""
# REQUIRED by house rule: every post ships with a mobile-friendly hero graphic
# or infographic. Place the file under static/img/posts/<slug>/ and set:
hero: "img/posts/<slug>/hero.png"
hero_alt: "One-line description of the image"
# Every draft also gets an AI-tells pass before publishing; see PUBLISHING.md.
---
