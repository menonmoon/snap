# Top 50 all-time Lens+ lenses: breakdown and winning formulas

Snapshot: 2026-10-10. Source: `ailc/charts/lenses?tab=top_overall` (the All-Time Top 50 on
easylens.snapchat.com), cross-checked with the other chart tabs. The chart is ranked over a
pool of **31,421** lenses, so the top 50 is the **top 0.16%**.

Data: `research/top-50-breakdown.json` (one row per lens), `research/chart-boards-2026-10-10.json`
(the 30-day, rising, debut and hit-rate boards), `research/top-50-classification.json` (manual
visual classification). Scripts: `research/scripts/`.

## Bottom line

1. **Two creators dominate.** @eren892 (DE) holds 12 of the 50, and @n-zw (SA) holds 5 more.
   eren892 also holds 12 spots in the last-30-day board, though only 5 lenses appear on both
   lists. The creator keeps placing new lenses, which is more durable than a single hit.
2. **Visual effects beat logic.** Colour grades, beauty looks, face warps, mirror panels,
   accessories, text cards and creature stickers make up 40 of the 50 (80%). Only 7 (14%) are
   interactive quiz or friends games.
3. **The strongest current formula is the stretch series.** Stretch-named lenses went from 5 to
   8 in the last 30 days, while 2013/2016-named lenses fell from 5 to 3. Beauty, glow and filter
   names went from 10 to 16. Those two are the current momentum.
4. **Quiz and friends games are a high-demand gap, but they are fading.** They are 8 of 50 in
   the all-time top 50 by chart tag (7 by our classification). In the 30-day board they drop to 2 of 50. They are still
   strong among new debuts (7 of 50), and the chart's own category tool flags Quiz and Bitmoji as
   under-supplied with high demand.
5. **Cheap beats complicated.** Scene-only grades (no face needed), text-card statements and
   sticker reactions need few or no scripts. About a quarter of the top 50 (13 of 50) have no
   script files at all.

## Method and limits

- **Categories.** The chart's own tags (Appearance, Video Effects, Aesthetic, Funny, Quiz,
  Friends, Reactions, Bitmoji, Pets, AI) are too coarse. We classified each lens by its visual
  mechanic, using its poster image and name, into 10 primary categories with sub-formats. Each
  lens also gets secondary tags. The classification is manual and rated high, medium or low
  confidence per lens (see `research/top-50-classification.json`).
- **Bundle features.** Each lens's `.lns` bundle was scanned for file names (LUT files,
  retouch masks, ML model files, face-warp shaders, script names). A bundled file means the
  feature ships with the lens. It does not prove a viewer triggers it. Default template files
  inflate some counts, so treat the LUT and retouch figures as "bundled", not "used".
- **Scores.** The boards expose `pct`, which is rank ÷ pool (a percentile), not a score. The
  rolling-30 board has an "Estimated Lens+ Score". The creator hit-rate board ranks creators but
  does not show the rate itself.
- **Survivorship.** We only see winners. Every formula below is a pattern among winners, not a
  guarantee.
- **Date caveat.** `createdDate` says Love Lineup Game and Soul Match were created 2026-10-02.
  Both sit in a board labelled May–Sep 2026. The field may be the latest publish date, so
  treat lens "age" as approximate.

## 1. Category breakdown (primary category, 50 lenses)

| Primary category | Lenses | Share | Ranks | Best | Median age (days)* | Scriptless |
|---|---|---|---|---|---|---|
| Colour grade | 12 | 24% | 2, 8, 9, 10, 19, 25, 26, 28, 33, 35, 41, 44 | #2 | 163 | 3 |
| Beauty & glam | 10 | 20% | 1, 12, 13, 14, 18, 22, 31, 32, 40, 43 | #1 | 170 | 2 |
| Interactive & quiz | 7 | 14% | 16, 20, 21, 23, 27, 30, 45 | #16 | 94 | 2 |
| Mirror & split panels | 6 | 12% | 7, 11, 24, 38, 42, 49 | #7 | 167 | 2 |
| Animal & creature | 3 | 6% | 3, 29, 48 | #3 | 182 | 3 |
| Face accessories | 3 | 6% | 4, 6, 46 | #4 | 147 | 0 |
| Text-card reaction | 3 | 6% | 5, 17, 37 | #5 | 168 | 1 |
| Face warp & distortion | 3 | 6% | 15, 36, 39 | #15 | 241 | 0 |
| Other / unclear | 2 | 4% | 47, 50 | #47 | 187 | 0 |
| AI stylise | 1 | 2% | 34 | #34 | 319 | 0 |

\* Age is from `createdDate`, with the caveat above.

Read across the table: quiz lenses are the youngest group (median 94 days). Face warps are the
oldest group with more than one lens (241 days). Big-bundle categories (face accessories, median about 2.6 MB) are heavier to
build than mirror panels (about 0.2 MB). Bundle size does not predict rank: the rank-vs-size
correlation is essentially zero (ρ = −0.04).

## 2. Subcategories, with lenses

### 2.1 Colour grade (12): the biggest category

- **Dazz series (n-zw).** #2 Dazz Cam X, #9 Dazz Vibe, #44 Dazz Vintage. Cool tone, sunglasses
  portraits, sometimes grain. Lenses from one series reach the top together.
- **Warm and golden.** #8 Summer Tanning, #19 Classic-Light, #28 Bold stroke, #41 CineReal Glow.
- **Soft, romantic or retro tint.** #25 Affection, #26 2016 Lite, #33 VNTG-35.
- **Scene only, no face needed.** #10 Pleasan Filter (saturated landscape), #35 4k (sharpened
  landscape). These are cheap to build and do not need face tracking.

### 2.2 Beauty & glam (10)

- **Natural and soft glam.** #12 No Makeup > (n-zw), #14 Light Filter MI (n-zw), #1 BEEN HER!,
  #32 Peach Fuzz, #40 Good Light.
- **Makeup and lashes.** #13 2016 + lashes (eren892), #22 Lash Light Touch, #31 Sugar Wink
  (winged liner), #18 Dream Contour (contour and glow).
- **Hair.** #43 Hair Colour (palette UI for recolouring).

### 2.3 Interactive & quiz (7)

- **Friends-based games.** #20 Love Lineup Game (multi-choice relationship game), #21 Soul Match
  (match meter), #30 Guess The Birthday (trivia with friends), #23 Letter to a friend (Bitmoji
  letter card), #45 Your Fate Squad (friend prediction).
- **Solo tap-to-reveal confessions.** #16 I'm Single Because, #27 Biggest Mistake ? (both
  @nemo_axo). Text plus tap reveal, no friend graph.

### 2.4 Mirror & split panels (6)

- **Mirror duplicates.** #7 Nashville Stretch, #11 2013 Stretched v2, #42 2016 Nerd Stretch,
  #38 Autizmen Stretch. Two copies of the face side by side, retro tint, often with stretch.
- **Stacked triptychs.** #49 2016 Eyes (eye close-ups), #24 Iconic Gaze (black-and-white eyes and
  lips).

### 2.5 Face accessories (3): all three by eren892

- #4 mustache + tattoos, #46 mustache + beanie, #6 Soulja Boy (text-printed sunglasses and cap).
- Among the heaviest bundles in the list (median about 2.6 MB), so accessories carry the most assets.

### 2.6 Face warp & distortion (3)

- #15 Funny smile12 (exaggerated smile), #36 Sigma Face (full-face warp), #39 L2+78 (face widen).
  Warp is a single-effect lens, with few or no scripts.

### 2.7 Animal & creature (3)

- #3 Stretch Tongue Cat (person and cat side by side, both tongues out), #29 monkey (animal
  sticker with a person), #48 Lizard Lizard (3D creature gesture). All use a character as the hook.

### 2.8 Text-card reaction (3)

- #5 Opinions Muted (full-screen statement on black), #17 day vibes (caption over a scene),
  #37 damn those eyes (caption over an eye close-up). These are the cheapest lenses to make.

### 2.9 Other (2) and AI (1)

- #47 5+8 (a hand-raised gesture; effect unclear from the poster), #50 orthodontic (picture-in-
  picture inset; the name suggests teeth or braces). Both are low confidence.
- #34 Vrtc (painterly stylised portrait, tagged AI). One lens is too small a sample.

## 3. Creators and countries

- **eren892 (DE): 12 lenses** across seven categories. Seven carry the 2013 or 2016 year or
  "Stretch" in the name. Four are mirror panels and three are accessories. The creator also has
  12 lenses in the 30-day top 50, but only 5 lenses appear on both lists. The newer ones are
  stretch variants (Instant Stretched, Spider Cat Stretch, Nerd Cat Stretch). Their common
  ingredients: stretch or mirror, a retro tint, one accessory, and a series-style name.
- **n-zw (SA): 5 lenses** in the all-time top 50, and **8 in the 30-day board**. They work as a
  family: Dazz (3), No Makeup, Light Filter. Their lenses are light and beauty grades, and
  several have no scripts.
- **Two creators hold 17 of 50 (34%).** The other 33 spots go to 27 creators, so most creators
  have one lens on the list.
- **Countries:** SA 15, DE 14, IN 13, PK 5, US 2, AE 1. SA, DE and IN together hold 84%. The
  chart does not show whether these are audience or creator location.

## 4. What the bundles contain (feature prevalence, 50 lenses)

| Feature signal (file names in bundle) | Lenses |
|---|---|
| LUT / colour correction files | 36 |
| Retouch / beauty mask files | 35 |
| ML model files (`.dnn`) | 21 |
| Face-warp shaders (graph warp, morphing) | 19 |
| 3D mesh files | 11 |
| Custom font files (text overlays) | 9 |
| Makeup masks (blush, eyeliner, lip, brow) | 7 |
| Friends components | 4 |
| EasyLens block scripts | 5 |
| Bitmoji files | 2 |
| Audio files | 2 |

Scriptless lenses: 13 of 50. Lenses with scripts have about 1 to 4 script files in the median.
The highest counts are 143 for #43 (a colour-picker UI bundle) and 76 for #50. Most of the top
50 are built from visual layers, not logic.

## 5. Momentum: all-time vs the last 30 days vs rising vs debut

| Signal | All-time top 50 | Rolling 30-day top 50 | Most improved (50) | New debuts, 2026-09 (50) |
|---|---|---|---|---|
| eren892 lenses | 12 | 12 | — | — |
| n-zw lenses | 5 | 8 | — | — |
| Beauty, glow or filter names\* | 10 | 16 | — | — |
| Stretch-named lenses | 5 | 8 | — | — |
| 2013 or 2016 names | 5 | 3 | — | — |
| Quiz, friends or Bitmoji tags | 8 | 2 | 1 | 7 |
| Lenses tagged EasyLens (`madeWith`) | 0 | 0 | 35 | 28 |
| Overlap with all-time top 50 | — | 23 of 50 | — | — |

\* Name families are keyword matches (for example "stretch", "2013|2016", and "dazz|glow|filter|makeup|beauty|skin|light|aesthetic|clean|radiance"). Counts are approximate.

Reading the table:

- **Beauty and stretch are gaining.** Both grow in the 30-day board. Retro-year names shrink
  while stretch grows, so the retro tint is moving toward stretch variants.
- **Quiz and friends are losing in the 30-day window**, though they are still common among
  new debuts. Both signals are real, so quizzes are a high-variance bet.
- **EasyLens is the production route of the rising cohort.** Most-improved creators and new
  debuts are mostly EasyLens-built. None of the all-time top 50 is tagged EasyLens in the
  metadata. The bundle scan finds EasyLens block scripts in 5 of 50, so the metadata may be
  incomplete. This points to a fast-growing no-code route, not a proven one.

## 6. Winning formulas

Each formula lists its ingredients, the evidence, and how sure we are. Strength reflects both
volume and persistence across boards, and it is still correlation among winners.

### F1. Retro stretch series (strength: high)

- **Ingredients:** a face warp or a mirror duplicate, a 2013 or 2016 tint, one accessory (mustache,
  lashes or glasses), and a series name ("2013 Stretched", "2016 + lashes", "… Stretch").
- **Evidence:** 12 of 50 all-time and 12 of 50 in the 30-day board, all by eren892 (5 lenses on
  both lists). Stretch names went from 5 to 8. 2013/2016 names fell from 5 to 3, so the newer
  momentum is in stretch variants, with the year tint kept less often.
- **Build:** a Face Stretch or graph-warp component, then a mirror duplicate using a flipped copy,
  then a colour grade, then an accessory overlay. See the `lenses/lash-glam` project in this repo
  for the accessory part.

### F2. Dazz and natural-beauty grade (strength: high)

- **Ingredients:** a light or no-face grade, a one-word series name ("Dazz", "No Makeup",
  "Light Filter", "Good Light"), and no heavy effects.
- **Evidence:** n-zw has 5 all-time and 8 in the 30-day board. Beauty and filter names went from
  10 to 16.
- **Build:** a colour LUT or colour correction plus a soft beauty layer. This is the cheapest
  formula with strong momentum.

### F3. Scene-only grade (strength: medium)

- **Ingredients:** a saturated landscape or environment grade, no face tracking.
- **Evidence:** #10 Pleasan Filter, #35 4k in the all-time list. Pleasant Vivid, HD and HD+ in the
  30-day board. PLEASANT YP is #2 on the most-improved board (+20.4 pp). The "Pleasant" family
  spans several creators.
- **Build:** a single post-effect grade. Lowest build cost in the list.

### F4. Face accessory overlay (strength: medium)

- **Ingredients:** a facial-hair, headwear, tattoo or lash overlay anchored to the face, with a
  name that lists the items ("mustache + beanie").
- **Evidence:** three all-time, all eren892. Appearance is the top chart tag (17 lenses). The
  "mustache + tattoos" lens is also in the 30-day board.
- **Build:** the head attachment and overlay components. The projects in `lenses/` implement this.

### F5. Quiz and friends game (strength: medium, high variance)

- **Ingredients:** a friend-based prompt (match %, trivia, relationship choice), a Bitmoji or
  friends element, and a result card.
- **Evidence:** 7 of 50 all-time by our classification (8 by chart tag), 7 of 50 debuts by chart
  tag, and the chart marks Quiz and Bitmoji as under-supplied with high demand. But 2 of 50 in the
  30-day board.
- **Build:** the largest build of the formulas. Only worth it if you can test with friends.

### F6. Animal or creature sticker reaction (strength: medium)

- **Ingredients:** a character (animal, creature) as the hook, a gesture or expression, and a
  short text.
- **Evidence:** #3, #29, #48 in the all-time top 50. New 30-day entries include ghostface sticker
  and Dewey Reactions.
- **Build:** a 3D sticker with a simple trigger. Low script count.

### F7. Text-card statement (strength: low to medium)

- **Ingredients:** one bold line of text over a plain or dark background, optionally over the
  face.
- **Evidence:** #5 Opinions Muted (also #9 in the 30-day board), #17 day vibes, #37 damn those eyes.
- **Build:** text overlay only. Cheapest lens to make, but fewer examples.

## 7. Recipe: what the top 50 has in common

1. **Hook in the first second.** Each poster has one readable image: a face warp, a mirror copy,
   a bold statement or a character.
2. **One visual change, not three.** Most lenses stack at most two effects (a grade plus a
   warp, or a grade plus an accessory).
3. **Series naming.** Lens names repeat a family word ("Dazz", "2016", "Stretch", "Pleasan").
   The top creators publish families, not one-offs.
4. **Retro or beauty tints.** Blue, purple or warm grades are common. The 2013 and 2016 tints
   are the most distinctive.
5. **Small scope.** Mirror panels and text cards are the smallest bundles. Heavy bundles
   (accessories) are the exception.

## 8. Next lenses to build, ranked by evidence

1. **Dazz-style beauty grade (F2):** strongest momentum, cheapest to build.
2. **Retro stretch mirror (F1):** strongest total evidence, moderate build.
3. **Scene grade (F3):** lowest effort, medium evidence.
4. **Quiz with friends (F5):** only if you can test multiplayer.

## 9. Open questions

- Confirm the EasyLens metadata. Does `madeWith` tag only some lenses?
- Confirm `createdDate` meaning (creation or latest publish) before using age.
- Verify the classification with the lens running in Lens Studio. The poster-based labels are
  unverified.
- The creator hit-rate board ranks creators without showing the rate. The rate would show whether
  small-volume creators are inflating the list.
- Check whether the Games niche (very high hit rate in `chart-boards`) is worth pursuing.
  It is outside the top 50, so it is not covered by these formulas.
