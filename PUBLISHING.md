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
2. AI-tells pass completed (see below). No exceptions.
3. `description` written: 1-2 sentences in front matter. This becomes the
   search-result snippet and the social preview text; never ship a post on
   the site-wide default.
4. Tags set (2-4, lowercase).
5. Proofread once on a phone.

## AI-tells review

Every draft gets a dedicated second pass for AI tells before it ships. The
blog is written in a practitioner's voice; anything that reads as
machine-generated fails the review, no matter how polished it sounds.

**Banned vocabulary.** Cut or replace: delve, tapestry, landscape
(metaphorical), leverage, utilize, robust, seamless, cutting-edge,
state-of-the-art, empower, unlock, elevate, harness, foster, navigate
(metaphorical), realm, embark, myriad, plethora, pivotal, multifaceted,
intricate, nuanced, crucial, vital, transformative, groundbreaking,
revolutionize, game-changer, paradigm shift, ecosystem (non-technical),
streamline, synergy, resonate, testament, journey, intricate.

**Banned openers and throat-clearing.** In today's fast-paced world, in this
day and age, now more than ever, in conclusion, in summary, it's worth noting
that, it's important to note that, let's dive in, let's unpack this, here's
the thing, here's why, the reality is, at the end of the day, picture this,
have you ever wondered, when it comes to.

**Structural tells.**
- No em-dashes. Use a period, comma, colon, or parentheses.
- No reflexive both-sides hedging ("on one hand X, on the other hand Y").
  If there's a view, lead with it.
- Lists only for genuinely parallel items (steps, options, criteria). Never
  turn one flowing thought into a tidy list of three, and never tack "Key
  takeaways" onto the end.
- No moralizing closing paragraph. End on the point, not a sermon.
- Vary sentence length. Human writing breathes.

**The read-aloud test.** Read the draft out loud. If it sounds like a
keynote, rewrite it until it sounds like a person.
