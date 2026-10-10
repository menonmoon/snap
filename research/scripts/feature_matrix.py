"""Build a per-lens feature matrix from Snap .lns bundles and the chart JSON.

Inputs:
  --chart   chart API JSON (ailc/charts/lenses?tab=top_overall)
  --lns     directory with one <rank>.lns bundle per lens (not committed)
Output:
  --out     JSON with one record per lens

Feature flags come from file names embedded in each bundle. A bundled file
means the feature ships with the lens, not that a viewer ever triggers it.
"""
import argparse, glob, json, os, re, statistics

PATH_RE = re.compile(rb'/[A-Za-z0-9_\-./ ]{3,120}\.[A-Za-z0-9]{2,5}')

FLAGS = {
    'lut_color_grade':   r'(?i)lookup\.png|color_?correction',
    'beauty_retouch':    r'retouch_mask|Basic Beauty ML|ML Retouch',
    'makeup_masks':      r'mask_(blush|eyeshadow|eyeliner|lip|eyebrow)|MakeupController|Makeup\.js',
    'face_warp':         r'(?i)graph_?warp|morphing|blendshapesetter',
    'ml_model_dnn':      r'\.dnn',
    'body_tracking':     r'(?<![A-Za-z])Body\.js|BodyLandmark',
    'face_expression':   r'FaceExpressionGetter',
    'mesh_3d':           r'\.mesh',
    'audio':             r'\.mp3|\.wav|\.m4a',
    'custom_font_text':  r'\.ttf|\.otf',
    'friends_component': r'FriendsComponent|FriendItemView|FriendsCarousel',
    'bitmoji':           r'Bitmoji',
    'easylens_template': r'BaseEasyLensBlock|EntryPointController|CmsTemplatesProvider|CmsAiController',
    'ai_clips':          r'AI Clips',
    'remote_api':        r'BasicRemoteApi|ApiService|RemoteApi',
}


def load_bundle_names(path):
    data = open(path, 'rb').read()
    paths = sorted(set(m.decode('latin1').strip() for m in PATH_RE.findall(data)))
    js = sorted(set(os.path.basename(p) for p in paths if p.endswith('.js')))
    return data, paths, js


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--chart', required=True)
    ap.add_argument('--lns', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    chart = json.load(open(a.chart))
    total = chart['total']
    records = []
    for lens in chart['lenses']:
        rank = lens['rank']
        bundle = os.path.join(a.lns, f'{rank:02d}.lns')
        data, paths, js = load_bundle_names(bundle)
        blob = '\n'.join(paths) + '\n' + '\n'.join(js)
        flags = {k: bool(re.search(p, blob)) for k, p in FLAGS.items()}
        records.append({
            'rank': rank,
            'lensId': lens['lensId'],
            'name': lens['name'],
            'creator': lens['username'],
            'country': lens['country'],
            'created': lens['createdDate'],
            'api_categories': lens['categories'],
            'percentile_of_pool': round(rank / total * 100, 4),
            'bundle_bytes': len(data),
            'script_files': len(js),
            'scriptless': len(js) == 0,
            'flags': flags,
        })
    json.dump({'pool_total': total, 'lenses': records}, open(a.out, 'w'), indent=1)

    # Summaries printed for review
    n = len(records)
    print(f'lenses={n} pool_total={total}')
    for k in FLAGS:
        c = sum(r['flags'][k] for r in records)
        print(f'  {k:<18} {c:>2}/{n}')
    print('  scriptless        ', sum(r['scriptless'] for r in records), '/', n)
    tiers = {'top10': records[:10], 'ranks11-25': records[10:25], 'ranks26-50': records[25:]}
    for t, rs in tiers.items():
        print(f"{t:<12} median_bytes={statistics.median(r['bundle_bytes'] for r in rs):>9.0f} "
              f"median_scripts={statistics.median(r['script_files'] for r in rs):>5.1f} "
              f"scriptless={sum(r['scriptless'] for r in rs)}/{len(rs)} "
              f"easylens={sum(r['flags']['easylens_template'] for r in rs)}/{len(rs)}")


if __name__ == '__main__':
    main()
