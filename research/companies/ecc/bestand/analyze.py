#!/usr/bin/env python3
"""ECC-Bestandsprofil: nur Aggregate aus einer lokal berechtigten CSV.
Usage: python3 analyze.py --input /path/source.csv --output /path/aggregates.json
Keine Einzelkunden, VSN, VMT-IDs, Berufs- oder Risikotexte werden ausgegeben.
"""
import argparse, csv, hashlib, json, re, sqlite3, statistics
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from decimal import Decimal
from pathlib import Path

STATUS_MAP = {'B':'beantragt','A':'aktiv','N':'beitragsfrei','H':'aktiv Honorar','S':'storniert','P':'abgelegt','E':'beantragt (DV)','F':'aktiv (DV)','R':'beitragsfrei (DV)','U':'in Bestandsübertragung','X':'aktiv ohne Betreuung','Y':'storniert (DV)','Z':'abgelegt (DV)','K':'aktiv Korrespondenz','V':'in Komplettübertragung'}
STATUS_GROUPS = {'aktiv':{'A','F','H','X','K'},'storniert':{'S','Y'},'abgelegt':{'P','Z'},'beitragsfrei':{'N','R'},'beantragt':{'B','E'},'in_uebertragung':{'U','V'}}
MISSING = {'', '-'}
FACTORS = {'monatlich': 12, 'vierteljährlich': 4, 'halbjährlich': 2, 'jährlich': 1}
DATE_FIELDS = ['Beginn','Ablauf','Antrag','Stornodatum','Erster Login (simplr)','Letzter Login (simplr)']
EXPECTED = ['VMT','Kundennr.','Vorname / Ansprechpartner','Alter','Beruf','Erster Login (simplr)','Letzter Login (simplr)','VSN','Sparte','Risiko','Art','Vorversicherung','Gesellschaft','Agentur','Beginn','Ablauf','Antrag','Stornodatum','Zahlweise','Netto-Beitrag','Brutto-Beitrag']

def money(v):
    if not re.fullmatch(r'-?(?:\d{1,3}(?:\.\d{3})+|\d+)(?:,\d+)?', v):
        raise ValueError('Invalid money format; no raw value exposed')
    return Decimal(v.replace('.','').replace(',','.'))

def dt(v):
    return None if v in MISSING else datetime.strptime(v,'%d.%m.%Y').date()

def pct(n,d): return round(100*n/d,4) if d else None

def amount(n): return str(n.quantize(Decimal('0.01')))

def concentration(values):
    vals=sorted(values,reverse=True); total=sum(vals)
    return {'groups':len(vals),'top1_pct':pct(float(sum(vals[:1])),float(total)),
            'top5_pct':pct(float(sum(vals[:5])),float(total)),
            'top10_pct':pct(float(sum(vals[:10])),float(total))}

def summarize(rows):
    recurring=[r for r in rows if r['Zahlweise'] in FACTORS]
    once=[r for r in rows if r['Zahlweise']=='einmalig']
    return {'rows':len(rows),'customers':len({r['Kundennr.'] for r in rows}),
            'vmt_count':len({r['VMT'] for r in rows}),
            'zero_net_rows':sum(r['_net']==0 for r in rows),
            'storno_date_present':sum(r['_Stornodatum'] is not None for r in rows),
            'recurring_rows':len(recurring),'one_off_rows':len(once),
            'scenario_annual_net':amount(sum((r['_net']*FACTORS[r['Zahlweise']] for r in recurring),Decimal(0))),
            'scenario_annual_gross':amount(sum((r['_gross']*FACTORS[r['Zahlweise']] for r in recurring),Decimal(0))),
            'one_off_net':amount(sum((r['_net'] for r in once),Decimal(0))),
            'one_off_gross':amount(sum((r['_gross'] for r in once),Decimal(0)))}

def dimension(rows,field):
    groups=defaultdict(list)
    for r in rows:groups[r[field] or '(leer)'].append(r)
    return {k:summarize(v) for k,v in sorted(groups.items(),key=lambda kv:(-len(kv[1]),kv[0]))}

def distribution(values,bounds):
    out=Counter()
    for n in values:
        out[next(label for upper,label in bounds if n<=upper)]+=1
    return dict(out)

def customers(rows,asof):
    groups=defaultdict(list)
    for r in rows:groups[r['Kundennr.']].append(r)
    ages=[]; age_missing=0; age_conflict=0; logins=[]; login_missing=0; login_conflict=0
    for rr in groups.values():
        age={r['Alter'] for r in rr if r['Alter'] not in MISSING}
        if len(age)==1:ages.append(int(next(iter(age))))
        elif not age:age_missing+=1
        else:age_conflict+=1
        login={r['_Letzter Login (simplr)'] for r in rr if r['_Letzter Login (simplr)'] is not None}
        if not login:login_missing+=1
        else:logins.append(max(login))
        if len(login)>1:login_conflict+=1
    counts=[len(rr) for rr in groups.values()]
    eligible={k:rr for k,rr in groups.items() if len({r['Alter'] for r in rr})==1 and rr[0]['Alter'] not in MISSING and 18<=int(rr[0]['Alter'])<=64}
    coverage={s:len({r['Kundennr.'] for r in rows if r['Sparte']==s}) for s in ['Privathaftpflicht','Hausrat','BU','Rente','PKW','RS','KV-Zusatz','PKV','Risikoleben','Grundfähigkeiten','bAV','Riesterrente']}
    return {'count':len(groups),'mean_rows_per_customer':round(statistics.mean(counts),4),
        'median_rows_per_customer':statistics.median(counts),'max_rows_per_customer':max(counts),
        'row_count_distribution':distribution(counts,[(1,'1'),(2,'2'),(3,'3'),(5,'4-5'),(10,'6-10'),(float('inf'),'11+')]),
        'age_valid_customers':len(ages),'age_missing_customers':age_missing,'age_conflicting_customers':age_conflict,
        'age_median':statistics.median(ages),'age_mean':round(statistics.mean(ages),4),
        'age_bands':distribution(ages,[(17,'unter18'),(24,'18-24'),(34,'25-34'),(44,'35-44'),(54,'45-54'),(64,'55-64'),(float('inf'),'65+')]),
        'last_login_missing_customers':login_missing,'last_login_conflicting_customers':login_conflict,
        'last_login_present_customers':len(logins),
        'last_login_within_30_days':sum(asof-timedelta(days=29)<=d<=asof for d in logins),
        'last_login_within_90_days':sum(asof-timedelta(days=89)<=d<=asof for d in logins),
        'last_login_within_365_days':sum(asof-timedelta(days=364)<=d<=asof for d in logins),
        'coverage_customers':coverage,'customers_age18_64':len(eligible),
        'age18_64_without_BU_row':sum(not any(r['Sparte']=='BU' for r in rr) for rr in eligible.values()),
        'age18_64_without_BU_or_LV_BUZ_row':sum(not any(r['Sparte'] in {'BU','LV mit BUZ'} for r in rr) for rr in eligible.values()),
        'customers_multiple_vmt':sum(len({r['VMT'] for r in rr})>1 for rr in groups.values()),
        'occupation_missing_customers':sum(all(r['Beruf'] in MISSING for r in rr) for rr in groups.values())}

def analyze(input_path,asof):
    b=input_path.read_bytes()
    with input_path.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f,delimiter=';'); assert reader.fieldnames==EXPECTED
        original=list(reader)
    assert all(set(r)==set(EXPECTED) and None not in r.values() for r in original)
    raw=[{k:v.strip() for k,v in r.items()} for r in original]
    exact=Counter(tuple(r[k] for k in EXPECTED) for r in original)
    normalized=Counter(tuple(r[k] for k in EXPECTED) for r in raw)
    for r in raw:
        r['_net']=money(r['Netto-Beitrag']); r['_gross']=money(r['Brutto-Beitrag'])
        for f in DATE_FIELDS:r['_'+f]=dt(r[f])
    # No destructive deduplication; exact-only alternative is separate.
    seen=set(); unique=[]
    for i,r in enumerate(raw):
        key=tuple(original[i][k] for k in EXPECTED)
        if key not in seen:unique.append(r);seen.add(key)
    out={'source':{'id':'ECC-BST-001','sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),
          'encoding':'UTF-8-SIG','delimiter':';','data_rows':len(raw),'columns':EXPECTED,'as_of':asof.isoformat()},
         'assumptions':{'status':'Legend ECC-BST-002: active A/F/H/X/K; X without servicing and K correspondence kept distinct. Status is not proof of current payment or ownership.',
           'money':'Scenario only: amounts assumed per payment period; currency absent; no revenue or valuation',
           'customer':'Kundennr. counted as an account, not verified unique person or household',
           'vmt':'VMT identifiers are not confirmed active sales partners'},
         'missingness':{f:sum(r[f] in MISSING for r in raw) for f in EXPECTED},
         'distinct_nonmissing':{f:len({r[f] for r in raw if r[f] not in MISSING}) for f in EXPECTED},
         'duplicates':{'exact_extra':sum(n-1 for n in exact.values()),'exact_groups':sum(n>1 for n in exact.values()),
                       'trimmed_extra':sum(n-1 for n in normalized.values())},
         'all':summarize(raw),'exact_unique':summarize(unique),'art':dimension(raw,'Art'),
         'payment_frequency':dimension(raw,'Zahlweise'),'sparte':dimension(raw,'Sparte'),
         'customers_all':customers(raw,asof)}
    for fields in [('VSN',),('Gesellschaft','VSN'),('Kundennr.','Gesellschaft','VSN'),('Kundennr.','Gesellschaft','VSN','Sparte')]:
        c=Counter(tuple(r[k] for k in fields) for r in raw if r['VSN'] not in MISSING)
        out['duplicates']['+'.join(fields)]={'groups':sum(n>1 for n in c.values()),'extra':sum(n-1 for n in c.values()),'affected_rows':sum(n for n in c.values() if n>1)}
    A=[r for r in raw if r['Art']=='A']
    assert set(r['Art'] for r in raw)<=set(STATUS_MAP)
    out['status_legend']={k:{'label':v,'rows':sum(r['Art']==k for r in raw),'source':'ECC-BST-002'} for k,v in STATUS_MAP.items()}
    out['status_groups']={k:summarize([r for r in raw if r['Art'] in codes]) for k,codes in STATUS_GROUPS.items()}
    active=[r for r in raw if r['Art'] in STATUS_GROUPS['aktiv']]
    active_afh=[r for r in raw if r['Art'] in {'A','F','H'}]
    active_keys=Counter((r['Kundennr.'],r['Gesellschaft'],r['VSN'],r['Sparte']) for r in active if r['VSN'] not in MISSING)
    out['active_possible_duplicate_keys']={'groups':sum(n>1 for n in active_keys.values()),'extra':sum(n-1 for n in active_keys.values()),'affected_rows':sum(n for n in active_keys.values() if n>1)}
    out['active_exact_unique']=summarize([r for r in unique if r['Art'] in STATUS_GROUPS['aktiv']])
    out['active_AFH']=summarize(active_afh)
    out['active_customers']=customers(active,asof)
    out['active_AFH_customers']=customers(active_afh,asof)
    out['active_sparte']=dimension(active,'Sparte')
    out['active_AFH_sparte']=dimension(active_afh,'Sparte')
    out['active_companies_top30']=dict(list(dimension(active,'Gesellschaft').items())[:30])
    out['active_payment_frequency']=dimension(active,'Zahlweise')
    out['active_checks']={'storno_past_or_today':sum(r['_Stornodatum'] is not None and r['_Stornodatum']<=asof for r in active),
        'storno_future':sum(r['_Stornodatum'] is not None and r['_Stornodatum']>asof for r in active),
        'begin_missing':sum(r['_Beginn'] is None for r in active),'begin_future':sum(r['_Beginn'] is not None and r['_Beginn']>asof for r in active),
        'expiry_before_today':sum(r['_Ablauf'] is not None and r['_Ablauf']<asof for r in active)}
    active_nostorno=[r for r in active if r['_Stornodatum'] is None or r['_Stornodatum']>asof]
    active_begun=[r for r in active_nostorno if r['_Beginn'] is not None and r['_Beginn']<=asof]
    out['active_no_past_storno']=summarize(active_nostorno)
    out['active_begun_no_past_storno']=summarize(active_begun)
    out['active_begun_no_past_storno_no_past_expiry']=summarize([r for r in active_begun if r['_Ablauf'] is None or r['_Ablauf']>=asof])
    out['active_customer_overlap']={'only_X_K_without_A_F_H':len({r['Kundennr.'] for r in active}-{r['Kundennr.'] for r in active_afh}),
        'all_customers_without_active_status':len({r['Kundennr.'] for r in raw}-{r['Kundennr.'] for r in active})}
    no_income=STATUS_GROUPS['beitragsfrei']|STATUS_GROUPS['storniert']|STATUS_GROUPS['abgelegt']
    out['no_active_or_pending_or_transfer_customers']=len({r['Kundennr.'] for r in raw}-{r['Kundennr.'] for r in raw if r['Art'] not in no_income})
    out['A']=summarize(A);out['A_exact_unique']=summarize([r for r in unique if r['Art']=='A'])
    out['sparte_A']=dimension(A,'Sparte');out['customers_A']=customers(A,asof)
    out['companies_all_top30']=dict(list(dimension(raw,'Gesellschaft').items())[:30])
    out['companies_A_top30']=dict(list(dimension(A,'Gesellschaft').items())[:30])
    out['sparte_by_art']={s:dict(Counter(r['Art'] for r in raw if r['Sparte']==s)) for s in sorted({r['Sparte'] for r in raw})}
    out['concentration']={}
    for label,rows in [('all',raw),('A',A),('active',active),('active_AFH',active_afh)]:
        vmt=Counter(r['VMT'] for r in rows)
        contributions=defaultdict(Decimal)
        for r in rows:
            if r['Zahlweise'] in FACTORS:contributions[r['VMT']]+=r['_net']*FACTORS[r['Zahlweise']]
        out['concentration'][label]={'vmt_rows':concentration(vmt.values()),'vmt_annual_net_scenario':concentration(contributions.values()),
             'company_rows':concentration(Counter(r['Gesellschaft'] for r in rows).values()),
             'vmt_size_distribution':distribution(vmt.values(),[(9,'1-9'),(49,'10-49'),(99,'50-99'),(499,'100-499'),(float('inf'),'500+')])}
    out['date_quality']={}
    for f in DATE_FIELDS:
        ds=[r['_'+f] for r in raw if r['_'+f] is not None]
        out['date_quality'][f]={'present':len(ds),'min':min(ds).isoformat(),'max':max(ds).isoformat(),
                               'before_1900':sum(d.year<1900 for d in ds),'after_2100':sum(d.year>2100 for d in ds),
                               'future':sum(d>asof for d in ds)}
    out['quality']={'net_zero':sum(r['_net']==0 for r in raw),'gross_less_than_net':sum(r['_gross']<r['_net'] for r in raw),
        'net_negative':sum(r['_net']<0 for r in raw),'gross_negative':sum(r['_gross']<0 for r in raw),
        'storno_before_begin':sum(r['_Stornodatum'] is not None and r['_Beginn'] is not None and r['_Stornodatum']<r['_Beginn'] for r in raw),
        'expiry_before_begin':sum(r['_Ablauf'] is not None and r['_Beginn'] is not None and r['_Ablauf']<r['_Beginn'] for r in raw),
        'last_login_before_first':sum(r['_Letzter Login (simplr)'] is not None and r['_Erster Login (simplr)'] is not None and r['_Letzter Login (simplr)']<r['_Erster Login (simplr)'] for r in raw)}
    cancel_buckets=defaultdict(list)
    for r in raw:
        d=r['_Stornodatum']
        key='missing' if d is None else ('before1900' if d.year<1900 else ('past_or_today' if d<=asof else 'future'))
        cancel_buckets[key].append(r)
    out['storno_date_buckets']={k:summarize(v) for k,v in cancel_buckets.items()}
    out['A_checks']={'storno_past_or_today':sum(r['_Stornodatum'] is not None and r['_Stornodatum']<=asof for r in A),
                     'storno_future':sum(r['_Stornodatum'] is not None and r['_Stornodatum']>asof for r in A),
                     'begin_missing':sum(r['_Beginn'] is None for r in A),'begin_future':sum(r['_Beginn'] is not None and r['_Beginn']>asof for r in A),
                     'expiry_before_today':sum(r['_Ablauf'] is not None and r['_Ablauf']<asof for r in A)}
    A_no_cancel=[r for r in A if r['_Stornodatum'] is None]
    A_not_ended=[r for r in A if (r['_Stornodatum'] is None or r['_Stornodatum']>asof) and r['_Beginn'] is not None and r['_Beginn']<=asof]
    out['A_no_storno_date']=summarize(A_no_cancel)
    out['A_begun_no_past_storno']=summarize(A_not_ended)
    out['A_begun_no_past_storno_no_past_expiry']=summarize([r for r in A_not_ended if r['_Ablauf'] is None or r['_Ablauf']>=asof])
    out['dates_by_year']={}
    for f in ['Beginn','Antrag','Stornodatum']:
        out['dates_by_year'][f]=dict(sorted(Counter(str(r['_'+f].year) for r in raw if r['_'+f] is not None).items()))
    out['dates_2026_by_month']={}
    for f in ['Beginn','Antrag','Stornodatum']:
        out['dates_2026_by_month'][f]=dict(sorted(Counter(r['_'+f].strftime('%Y-%m') for r in raw if r['_'+f] is not None and r['_'+f].year==2026).items()))
    out['rente_active_companies_top10']=dict(list(dimension([r for r in active if r['Sparte']=='Rente'],'Gesellschaft').items())[:10])
    rente=[r for r in A if r['Sparte']=='Rente']
    out['rente_A_companies_top10']=dict(list(dimension(rente,'Gesellschaft').items())[:10])
    by_pay={k:[] for k in FACTORS}
    for r in A:
        if r['Zahlweise'] in by_pay:by_pay[r['Zahlweise']].append(r['_gross'])
    out['A_gross_by_payment_quantiles']={k:{'rows':len(v),'median':amount(Decimal(statistics.median(v))),'max':amount(max(v))} for k,v in by_pay.items() if v}
    cohorts=defaultdict(list)
    for r in raw:
        d=r['_Beginn']
        if d is not None:cohorts[str(d.year)].append(r)
    out['begin_cohorts_2019_2026']={year:{'rows':len(rr),'with_storno_on_or_before_asof':sum(r['_Stornodatum'] is not None and date(1900,1,1)<=r['_Stornodatum']<=asof for r in rr),
        'art_A':sum(r['Art']=='A' for r in rr)} for year,rr in sorted(cohorts.items()) if '2019'<=year<='2026'}
    # Independent SQL reconciliation uses cents instead of Decimal and its own grouping.
    con=sqlite3.connect(':memory:')
    con.execute('CREATE TABLE r(customer TEXT, art TEXT, sparte TEXT, net INTEGER, gross INTEGER, factor INTEGER)')
    con.executemany('INSERT INTO r VALUES(?,?,?,?,?,?)',[(r['Kundennr.'],r['Art'],r['Sparte'],int(r['_net']*100),int(r['_gross']*100),FACTORS.get(r['Zahlweise'],0)) for r in raw])
    sql=con.execute('SELECT COUNT(*),COUNT(DISTINCT customer),SUM(net*factor),SUM(gross*factor) FROM r').fetchone()
    assert sql==(len(raw),out['customers_all']['count'],int(Decimal(out['all']['scenario_annual_net'])*100),int(Decimal(out['all']['scenario_annual_gross'])*100))
    for art,n,s in con.execute('SELECT art,COUNT(*),SUM(net*factor) FROM r GROUP BY art'):
        assert n==out['art'][art]['rows'] and s==int(Decimal(out['art'][art]['scenario_annual_net'])*100)
    for key in ['art','sparte','payment_frequency']:
        assert sum(v['rows'] for v in out[key].values())==len(raw)
        assert sum(Decimal(v['scenario_annual_net']) for v in out[key].values())==Decimal(out['all']['scenario_annual_net'])
    assert sum(v['rows'] for v in out['storno_date_buckets'].values())==len(raw)
    assert sum(v['rows'] for v in out['status_groups'].values())==len(raw)
    assert sum(v['rows'] for v in out['active_sparte'].values())==len(active)
    for key in ['customers_A','customers_all','active_customers','active_AFH_customers']:
        c=out[key];assert sum(c['row_count_distribution'].values())==c['count']
        assert sum(c['age_bands'].values())+c['age_missing_customers']+c['age_conflicting_customers']==c['count']
    out['validation']={'csv_shape':'PASS','numeric_parse':'PASS','date_parse':'PASS (semantic anomalies remain)',
         'independent_sql_count_customers_money':'PASS','independent_sql_art_groups':'PASS','dimension_total_reconciliation':'PASS','customer_partition_reconciliation':'PASS'}
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--output',required=True,type=Path);p.add_argument('--as-of',default='2026-10-26')
    a=p.parse_args();result=analyze(a.input,date.fromisoformat(a.as_of));a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'rows':result['all']['rows'],'customers':result['customers_all']['count'],'A':result['A'],'validation':result['validation']},ensure_ascii=False))
