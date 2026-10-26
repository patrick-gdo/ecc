#!/usr/bin/env python3
"""ECC Beginnkohorten; schreibt ausschließlich aggregierte Kennzahlen."""
import argparse
import csv
import hashlib
import json
import sqlite3
from collections import Counter
from datetime import date, datetime
from pathlib import Path

GROUPS = {
    'Biometrie': ['BU', 'Risikoleben', 'Grundfähigkeiten', 'LV mit BUZ', 'DD', 'MultiRisk'],
    'Rente / bAV': ['Rente', 'bAV', 'Riesterrente'],
    'Sach': ['PKW', 'Privathaftpflicht', 'Hausrat', 'RS', 'Unfall', 'Wohngebäude', 'Krad', 'Glas', 'Anhänger', 'Hundehaftpflicht', 'Tierleben', 'Betriebshaftpflicht', 'Reise', 'LKW', 'HuG', 'Inhalt', 'Firmen-RS', 'VMH', 'gew. PKW', 'Elektronik', 'Traktor', 'Pferdehaftpflicht', 'gew. WGV', 'Wohnmobil', 'Jagdhaftpflicht', 'Berufshaftpflicht', 'Bauversicherung', 'Kaution', 'Tech', 'Boot', 'Cyber', 'Öltankhaftpflicht', 'Ertragsausfall', 'Transport'],
    'KV Zusatz': ['KV-Zusatz'],
    'KV Voll': ['PKV'],
}
STATUS_SETS = {'abgeschlossen_inkl_storniert': list('AFHNRSY'), 'nur_aktiv': list('AFH'), 'inkl_abgelegt_sensitivitaet': list('AFHNRSYPZ')}

def load(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f, delimiter=';')
        raw = list(reader)
        fields = reader.fieldnames
    assert len(fields) == 18 and len(set(fields)) == 18
    assert all(set(r) == set(fields) and all(v is not None for v in r.values()) for r in raw)
    rows = [{k: v.strip() for k, v in r.items()} for r in raw]
    dates = [datetime.strptime(r['Beginn'], '%d.%m.%Y').date().isoformat() for r in rows]
    meta = {'filename': path.name, 'bytes': path.stat().st_size, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'rows': len(rows), 'fields': fields, 'min_beginn': min(dates), 'max_beginn': max(dates), 'status_counts': dict(Counter(r['Art'] for r in rows)), 'begin_year_counts': dict(sorted(Counter(d[:4] for d in dates).items()))}
    return rows, dates, [tuple(r[f] for f in fields) for r in raw], meta

def rank(rows):
    out = {}
    for group, sparten in GROUPS.items():
        chosen = [r for r in rows if r['Sparte'] in sparten]
        counts = Counter(r['Gesellschaft'] or '(leer)' for r in chosen)
        ranked = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        listing = [{'company': c, 'rows': n, 'rank': 1 + sum(v > n for v in counts.values()), 'share_pct': round(n / len(chosen) * 100, 4)} for c, n in ranked]
        fifth = ranked[min(4, len(ranked)-1)][1] if ranked else 0
        out[group] = {'sparten': sparten, 'total_rows': len(chosen), 'companies': len(counts), 'ranking': listing, 'top5_with_ties': [r for r in listing if r['rows'] >= fifth], 'missing_company_rows': counts.get('(leer)', 0)}
    return out

def analyze(path, start, as_of, source_id):
    rows, dates, rawkeys, meta = load(path)
    inside = [r for r, d in zip(rows, dates) if start <= d <= as_of]
    inside_keys = [k for k, d in zip(rawkeys, dates) if start <= d <= as_of]
    cases = {}
    con = sqlite3.connect(':memory:')
    con.execute('CREATE TABLE rows (sparte TEXT, status TEXT, company TEXT, beginn TEXT)')
    con.executemany('INSERT INTO rows VALUES (?,?,?,?)', [(r['Sparte'], r['Art'], r['Gesellschaft'] or '(leer)', d) for r, d in zip(rows, dates)])
    for case, statuses in STATUS_SETS.items():
        selected = [r for r in inside if r['Art'] in statuses]
        selected_keys = [k for r, k in zip(inside, inside_keys) if r['Art'] in statuses]
        ranked = rank(selected)
        for group, sparten in GROUPS.items():
            query = 'SELECT company, COUNT(*) AS n FROM rows WHERE beginn >= ? AND beginn <= ? AND status IN (' + ','.join('?' for _ in statuses) + ') AND sparte IN (' + ','.join('?' for _ in sparten) + ') GROUP BY company ORDER BY n DESC, company'
            actual = con.execute(query, [start, as_of] + statuses + sparten).fetchall()
            assert actual == [(r['company'], r['rows']) for r in ranked[group]['ranking']]
        mapped = {s for sparten in GROUPS.values() for s in sparten}
        unmapped = dict(sorted(Counter(r['Sparte'] for r in selected if r['Sparte'] not in mapped).items()))
        assert sum(g['total_rows'] for g in ranked.values()) + sum(unmapped.values()) == len(selected)
        key_counts = Counter((r['Kundennr.'], r['Gesellschaft'], r['VSN'], r['Sparte']) for r in selected if r['VSN'] not in ('', '-'))
        cases[case] = {'statuses': statuses, 'rows': len(selected), 'status_counts': dict(Counter(r['Art'] for r in selected)), 'groups': ranked, 'unmapped_sparten': unmapped, 'exact_duplicate_extra_rows': len(selected_keys) - len(set(selected_keys)), 'candidate_contract_key_extra_rows': sum(n-1 for n in key_counts.values()), 'year_counts': dict(sorted(Counter(datetime.strptime(r['Beginn'], '%d.%m.%Y').strftime('%Y') for r in selected).items()))}
    con.close()
    main_statuses = STATUS_SETS['abgeschlossen_inkl_storniert']
    out = {'source_id': source_id, 'source': meta, 'start': start, 'as_of': as_of, 'before_start': sum(d < start for d in dates), 'after_as_of': sum(d > as_of for d in dates), 'date_eligible_rows': len(inside), 'date_eligible_status_counts': dict(Counter(r['Art'] for r in inside)), 'excluded_status_counts_in_period': dict(Counter(r['Art'] for r in inside if r['Art'] not in main_statuses)), 'exact_duplicate_extra_rows_all': len(rawkeys)-len(set(rawkeys)), 'cases': cases, 'validation': 'Alle Gesellschaftsrangfolgen in 5 Bereichen und 3 Statussichten: Python Counter = SQLite GROUP BY; Summen abgeglichen.'}
    assert out['before_start'] + out['after_as_of'] + len(inside) == len(rows)
    return out, rawkeys, dates

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--from-2024', required=True, type=Path)
    parser.add_argument('--from-2025', required=True, type=Path)
    parser.add_argument('--as-of', default='2026-10-26', type=date.fromisoformat)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    first, keys24, dates24 = analyze(args.from_2024, '2024-01-01', args.as_of.isoformat(), 'ECC-BST-003')
    second, keys25, _ = analyze(args.from_2025, '2025-01-01', args.as_of.isoformat(), 'ECC-BST-004')
    subset = Counter(k for k, d in zip(keys24, dates24) if d >= '2025-01-01')
    other = Counter(keys25)
    fields = first['source']['fields']
    assert fields == second['source']['fields']
    dims = [fields.index(k) for k in ['Sparte', 'Art', 'Gesellschaft', 'Beginn']]
    project = lambda counts: Counter({}) + Counter(v for k, n in counts.items() for v in [tuple(k[i].strip() for i in dims)] for _ in range(n))
    ranking_dimensions_equal = project(subset) == project(other)
    keycols = [fields.index(k) for k in ['Kundennr.', 'Gesellschaft', 'VSN', 'Sparte']]
    contract_key = lambda row: tuple(row[i] for i in keycols)
    diffs = []
    for old in (subset-other).elements():
        matches = [new for new in (other-subset).elements() if contract_key(new) == contract_key(old)]
        diffs.append({'matching_rows': len(matches), 'changed_fields': [[k for k, a, b in zip(fields, old, new) if a != b] for new in matches]})
    out = {'legend_id': 'ECC-BST-002', 'rank_by': 'contract_rows', 'date_basis': 'Beginn', 'company_normalization': 'none; whitespace trimmed', 'deduplication': 'none; duplicates reported', 'windows': [first, second], 'export_comparison': {'identical_multiset_2025_subset': subset == other, 'ranking_dimensions_equal': ranking_dimensions_equal, 'only_in_2024_subset_rows': sum((subset-other).values()), 'only_in_2025_export_rows': sum((other-subset).values()), 'changed_field_summary': diffs}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'windows': [{'start': w['start'], 'rows': w['cases']['abgeschlossen_inkl_storniert']['rows'], 'after_as_of': w['after_as_of'], 'excluded_status_counts': w['excluded_status_counts_in_period'], 'duplicates': w['cases']['abgeschlossen_inkl_storniert']['exact_duplicate_extra_rows'], 'candidate_key_extras': w['cases']['abgeschlossen_inkl_storniert']['candidate_contract_key_extra_rows'], 'groups': {g: {'total': v['total_rows'], 'top5': v['top5_with_ties']} for g, v in w['cases']['abgeschlossen_inkl_storniert']['groups'].items()}} for w in out['windows']], 'export_comparison': out['export_comparison']}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
