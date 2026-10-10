# Top paid lenses: what works and what we imitate

Source: `research/top-paid-lenses.json`, captured from the Lens+ All Time Top 50 chart
(`easylens.snapchat.com/topic/lens-plus-top-charts?chart=all-time`) on 2026-10-10.

The chart gives rank, name, creator, country and category tags. It does not give earnings or
usage numbers, so "successful" here means "ranked in the top 50 of the paid Lens+ chart".

## What the chart rewards

| Category tag | Lenses in top 50 |
|---|---|
| Appearance | 17 |
| Video Effects | 15 |
| Aesthetic | 12 |
| Funny | 11 |
| Quiz | 6 |
| Friends | 6 |
| Reactions | 3 |
| Bitmoji | 2 |
| Pets / AI | 1 each |

Creators matter as much as categories:

- **@eren892** (DE) has **12 of the 50**. Their lenses are retro face effects: "Stretch",
  "2013 / 2016" looks, lashes, and mustache and beanie accessories.
- **@n-zw** (SA) has 5 "Dazz" beauty and color lenses.
- Creators from SA, DE and IN fill 42 of the 50 spots.

## Formats, grouped

1. **Face accessories** (Appearance, Funny). Simple overlays anchored to the face: mustache,
   beanie, tattoos, lashes, hair color. Examples: `mustache + beanie` (#46), `mustache + tattoos`
   (#4), `2016 + lashes` (#13), `Lash Light Touch` (#22).
2. **Face stretch and retro warp** (Video Effects). Stretched faces with a retro look. Examples:
   `Nashville Stretch` (#7), `2013 Stretched v2` (#11), `2016 Nerd Stretch` (#42),
   `Autizmen Stretch` (#38), `Sigma Face` (#36).
3. **Beauty and aesthetic grading** (Aesthetic, Video Effects). Skin, glow and color grades.
   Examples: `Dazz Cam X` (#2), `Dazz Vibe` (#9), `No Makeup >` (#12), `Good Light` (#40).
4. **Quiz and friends games** (Quiz, Friends, Bitmoji). Interactive, shareable. Examples:
   `Love Lineup Game` (#20), `Soul Match` (#21), `Guess The Birthday` (#30).
5. **Reactions and funny** (Reactions, Funny, Pets). Short gags. Examples: `Opinions Muted` (#5),
   `Stretch Tongue Cat` (#3).

## What we imitate, and status

Imitations copy the *format and mechanic* that makes these lenses rank. The art is newly generated
and the names are our own. We do not copy other creators' assets, names or textures.

| Our lens | Imitates | Format | Status |
|---|---|---|---|
| `lenses/mustache-beanie` | #46 mustache + beanie, #4 mustache + tattoos | Face accessories | Assets generated, scripts type-checked. Not yet run in Lens Studio. |
| `lenses/lash-glam` | #13 2016 + lashes, #22 Lash Light Touch | Face accessories, symmetric | Asset generated, script type-checked. Not yet run in Lens Studio. |
| (next) stretch-retro | #7 Nashville Stretch, #11 2013 Stretched v2 | Face stretch | Not started. Face Stretch features are set in the Inspector, so the feature names need checking in the editor first. |
| (next) warm-vintage grade | #2 Dazz Cam X, #44 Dazz Vintage | Color grade | Not started. Needs a color or post-effect material. |
| (next) quiz game | #20 Love Lineup Game, #21 Soul Match | Quiz with friends | Not started. Largest scope: quiz logic plus the friends and Bitmoji flow. |

## Next steps, in priority order

1. Open the two accessory lenses in Lens Studio and confirm they render on a face. Tune sizes and
   anchor points in the Inspector.
2. Add the stretch-retro lens. It is the most common format on the chart (12 of 50 from one
   creator). Check the Face Stretch feature names in the editor first.
3. Add a warm-vintage color grade for the Dazz-style lenses.
4. Consider the quiz format last. It is the most work and needs multiplayer testing.
