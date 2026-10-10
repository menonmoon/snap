"""Image-asset profile for each lens bundle.

Reads the image file names embedded in each <rank>.lns bundle, drops files
shared by many lenses (Snap template defaults) and UI icons, then sorts what
remains into groups:
  custom_lut      colour lookup table image, rare across the chart
  overlay_texture grain, haze, gloss, glow or blend texture layers
  makeup_mask     lip, eye, blush, contour or face-mask images
  prop_art        stickers, accessories or cut-out art
  uploaded_photo  creator photos or uploaded asset files

Only counts and group flags are written. File names are not, because they
come from other creators' bundles.

Usage: python3 research/scripts/image_profile.py <lns_dir> <out.json>
"""
import collections
import json
import os
import re
import sys

LNS_DIR, OUT = sys.argv[1], sys.argv[2]
PATH_RE = re.compile(rb'/[A-Za-z0-9_\-./ ]{3,120}\.[A-Za-z0-9]{2,5}')
IMG_RE = re.compile(r'\.(png|jpe?g|pvr)$', re.I)
SHARED_THRESHOLD = 4  # a file in more than this many lenses is a template default

GROUPS = [
    ('custom_lut', r'lookup|\blut\b|_lut|LUT\.'),
    ('overlay_texture', r'overlay|grain|haze|gloss|glow|texture|blend|vignette|shimmer|tone'),
    ('makeup_mask', r'mask_|lip|lash|eye|blush|contour|brow|liner|makeup|face_?uv|opacity|facemask|cheek|nose'),
    ('prop_art', r'tattoo|sticker|removebg|mustache|beanie|glass|hat|crown|flower|heart|emoji|cat|monkey|lizard|ghost|sunglass'),
    ('uploaded_photo', r'^File_\d|^IMG_|^photo|PicsArt|Screenshot|^\d+\.(png|jpe?g)$|Resource\d|^Download|^[0-9a-f]{8}-|^[0-9a-f]{20,}'),
]
UI_RE = re.compile(r'button|icon|retry|title|avatar|check|shuffle|^User \d|loading|fallback|undo|arrow|label', re.I)

per_lens = {}
for rank in range(1, 51):
    data = open(os.path.join(LNS_DIR, f'{rank:02d}.lns'), 'rb').read()
    names = set()
    for m in PATH_RE.findall(data):
        base = os.path.basename(m.decode('latin1').strip())
        if IMG_RE.search(base):
            names.add(base)
    per_lens[rank] = names

freq = collections.Counter(n for s in per_lens.values() for n in s)
out = {}
for rank, names in per_lens.items():
    custom = [n for n in names if freq[n] <= SHARED_THRESHOLD and not UI_RE.search(n)]
    groups = {g: 0 for g, _ in GROUPS}
    for n in custom:
        for g, pat in GROUPS:
            if re.search(pat, n, re.I):
                groups[g] += 1
                break
    out[rank] = {
        'image_files': len(names),
        'custom_images': len(custom),
        **groups,
        'image_led': any(groups[g] for g in ('overlay_texture', 'makeup_mask', 'prop_art', 'uploaded_photo')),
        'no_custom_images': len(custom) == 0,
    }

json.dump(out, open(OUT, 'w'), indent=1)

n = 50
print('lenses with any custom image files:', sum(1 for r in out.values() if r['custom_images']))
print('lenses with a custom LUT:          ', sum(1 for r in out.values() if r['custom_lut']))
print('lenses with overlay/prop/upload:   ', sum(1 for r in out.values() if r['image_led']))
print('lenses with no custom images:      ', sum(1 for r in out.values() if r['no_custom_images']))
for g, _ in GROUPS:
    print(f'  {g:<17} lenses={sum(1 for r in out.values() if r[g])}')
print('no custom images at:', [r for r, v in out.items() if v['no_custom_images']])
print('wrote', OUT)
