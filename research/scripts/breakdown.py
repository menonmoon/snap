"""Join chart, bundle features and manual classification; print group summaries.

Usage:
  python3 research/scripts/breakdown.py <feature_matrix.json> <classification.json> <out.json>
"""
import datetime as dt
import json
import re
import statistics
import sys
from collections import Counter, defaultdict

fm = json.load(open(sys.argv[1]))
cls = {c['rank']: c for c in json.load(open(sys.argv[2]))['lenses']}
out_path = sys.argv[3]
TODAY = dt.date(2026, 10, 10)
POOL = fm['pool_total']

rows = []
for r in fm['lenses']:
    c = cls[r['rank']]
    created = dt.date.fromisoformat(r['created'])
    rows.append({**r, **{k: c[k] for k in ('primary', 'sub', 'secondary', 'hook', 'face', 'confidence')},
                 'age_days': (TODAY - created).days})

def med(xs):
    return statistics.median(xs) if xs else None

# 1. Primary category breakdown
by_cat = defaultdict(list)
for r in rows:
    by_cat[r['primary']].append(r)
cat_summary = []
for cat, rs in sorted(by_cat.items(), key=lambda kv: (-len(kv[1]), min(x['rank'] for x in kv[1]))):
    cat_summary.append({
        'category': cat,
        'count': len(rs),
        'share_pct': round(100 * len(rs) / len(rows), 1),
        'ranks': sorted(x['rank'] for x in rs),
        'best_rank': min(x['rank'] for x in rs),
        'median_age_days': med([x['age_days'] for x in rs]),
        'median_bundle_kb': round(med([x['bundle_bytes'] for x in rs]) / 1024),
        'scriptless': sum(x['scriptless'] for x in rs),
        'creators': Counter(x['creator'] for x in rs).most_common(),
        'subs': Counter(x['sub'] for x in rs).most_common(),
        'flag_rates': {k: sum(x['flags'][k] for x in rs) for k in rs[0]['flags']},
    })

print('== PRIMARY CATEGORIES (n=%d) ==' % len(rows))
for c in cat_summary:
    print(f"{c['category']:<26} n={c['count']:>2} ({c['share_pct']:>4}%) best=#{c['best_rank']:<2} "
          f"median_age={c['median_age_days']:>5}d kb={c['median_bundle_kb']:>5} scriptless={c['scriptless']} "
          f"ranks={c['ranks']}")
    print('    creators:', c['creators'][:4])
    print('    subs:', [f"{s}x{n}" for s, n in c['subs'][:6]])

# 2. Creator concentration
creator_counts = Counter(r['creator'] for r in rows)
print('\n== CREATORS with 2+ lenses ==')
for cr, n in creator_counts.most_common():
    if n < 2:
        break
    rs = sorted([r for r in rows if r['creator'] == cr], key=lambda x: x['rank'])
    print(f"@{cr:<14} n={n} ranks={[x['rank'] for x in rs]} cats={dict(Counter(x['primary'] for x in rs))}")
print('unique creators:', len(creator_counts), ' single-lens creators:', sum(1 for v in creator_counts.values() if v == 1))
top10_creators = Counter(r['creator'] for r in rows if r['rank'] <= 10)
print('top-10 creator mix:', dict(top10_creators))

# 3. Country
print('\n== COUNTRY ==')
cc = Counter(r['country'] for r in rows)
print(cc.most_common())
print('SA/DE/IN share:', round(100 * (cc['SA'] + cc['DE'] + cc['IN']) / len(rows), 1), '%')

# 4. Age / freshness
ages = [r['age_days'] for r in rows]
print('\n== AGE ==')
print('median age days', med(ages), 'min', min(ages), 'max', max(ages))
for lo, hi, label in [(0, 60, '<=60d'), (61, 180, '61-180d'), (181, 365, '181-365d'), (366, 10**6, '>365d')]:
    print(f'  {label:<10} {sum(lo <= a <= hi for a in ages)}')
fresh = sorted([r for r in rows if r['age_days'] <= 60], key=lambda x: x['rank'])
print('lenses created in last 60 days:', [(x['rank'], x['name'], x['created']) for x in fresh])
rho_x = [r['rank'] for r in rows]
def spearman(x, y):
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i]); rk = [0] * len(v)
        for i, idx in enumerate(s): rk[idx] = i + 1
        return rk
    rx, ry = rank(x), rank(y)
    n = len(x); d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))
print('spearman(rank, age_days) = %.3f  (positive => newer lenses sit lower)' % spearman(rho_x, ages))
print('spearman(rank, bundle_bytes) = %.3f' % spearman(rho_x, [r["bundle_bytes"] for r in rows]))

# 5. Feature prevalence overall and by primary category
print('\n== FEATURE PREVALENCE (bundle file signals, share of 50) ==')
keys = list(rows[0]['flags'].keys())
for k in keys:
    print(f"  {k:<18} {sum(r['flags'][k] for r in rows):>2}/50")

# 6. Series naming (lens-name families)
families = {
    'Dazz': r'dazz', '2013/2016 retro': r'\b20(13|16)\b', 'Stretch': r'stretch',
    'mustache': r'mustache', 'Lash': r'lash', 'Eyes': r'eyes', 'Filter/Light': r'filter|light',
    'Quiz-like Q/confession': r"single|mistake|guess|match|fate|lineup|soul",
}
print('\n== NAME FAMILIES ==')
for fam, pat in families.items():
    hits = [r for r in rows if re.search(pat, r['name'], re.I)]
    print(f"  {fam:<24} n={len(hits):>2} ranks={[x['rank'] for x in hits]} creators={dict(Counter(x['creator'] for x in hits))}")

json.dump({'categories': cat_summary, 'rows': rows, 'pool_total': POOL}, open(out_path, 'w'), indent=1, default=str)
print('\nwrote', out_path)
