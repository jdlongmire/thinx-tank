# Thinx-Tank publishing rules

## House rule: every article ships with a visual

Every published post **must** include a mobile-friendly hero graphic or
infographic. No exceptions. The visual is part of the article, not decoration.

- **Format:** hero graphic (1200x630 or larger) or an infographic that
  summarizes the post's key point.
- **Mobile-friendly:** legible and correctly cropped at 360px wide. Test on a
  phone viewport before publishing. Text in the image must remain readable.
- **Location:** `static/img/posts/<slug>/hero.png` (or `infographic.png`).
- **Front matter:** set `hero:` to the image path and `hero_alt:` to a
  one-line description. The theme renders it at the top of the post and it
  doubles as the social sharing image.
- **Alt text is required.** Every hero/infographic ships with `hero_alt`.

## Checklist before `draft: false`

1. Hero graphic or infographic present, mobile-checked, alt text written.
2. Tags set (2-4, lowercase).
3. Proofread once on a phone.
