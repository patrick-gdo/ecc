#!/usr/bin/env python3
"""Top-Gesellschaften nach Vertragszeilen; rein deskriptive Kategorienzuordnung."""
import argparse,csv,json,sqlite3,hashlib
from collections import Counter
from pathlib import Path

GROUPS={
'Biometrie':['BU','Risikoleben','Grundfähigkeiten','LV mit BUZ','DD','MultiRisk'],
'Rente / bAV':['Rente','bAV','Riesterrente'],
'Sach':['PKW','Privathaftpflicht','Hausrat','RS','Unfall','Wohngebäude','Krad','Glas','Anhänger','Hundehaftpflicht','Tierleben','Betriebshaftpflicht','Reise','LKW','HuG','Inhalt','Firmen-RS','VMH','gew. PKW','Elektronik','Traktor','Pferdehaftpflicht','gew. WGV','Wohnmobil','Jagdhaftpflicht','Berufshaftpflicht','Bauversicherung','Kaution','Tech','Boot','Cyber','Öltankhaftpflicht','Ertragsausfall','Transport'],
'KV Zusatz':['KV-Zusatz'],
'KV Voll':['PKV']}
STATUSES=['A','F','H']
def run(path):
 with path.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f,delimiter=';'))
 rows=[{k:v.strip() for k,v in r.items()} for r in rows]
 active=[r for r in rows if r['Art'] in STATUSES]
 con=sqlite3.connect(':memory:');con.execute('CREATE TABLE data (sparte TEXT, art TEXT, company TEXT)')
 con.executemany('INSERT INTO data VALUES (?,?,?)',[(r['Sparte'],r['Art'],r['Gesellschaft'] or '(leer)') for r in rows])
 out={'source_id':'ECC-BST-001','legend_id':'ECC-BST-002','source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'as_of':'2026-10-26','rank_by':'contract_rows','statuses':STATUSES,'company_normalization':'none; original labels',
 'interpretation':'Active inventory only; source does not prove original mediation. No cancellation date exclusion.',
 'groups':{},'unmapped_sparten':sorted({r['Sparte'] for r in active}-{s for values in GROUPS.values() for s in values})}
 for label,sparten in GROUPS.items():
  group=[r for r in active if r['Sparte'] in sparten]
  c=Counter(r['Gesellschaft'] or '(leer)' for r in group)
  ranked=sorted(c.items(),key=lambda x:(-x[1],x[0]))
  q='SELECT company, COUNT(*) AS n FROM data WHERE art IN (?,?,?) AND sparte IN ('+','.join('?'*len(sparten))+') GROUP BY company ORDER BY n DESC,company'
  assert con.execute(q,STATUSES+sparten).fetchall()==ranked
  out['groups'][label]={'sparten':sparten,'total_rows':len(group),'companies':len(c),'top5':[{'company':k,'rows':v,'share_pct':round(v/len(group)*100,4)} for k,v in ranked[:5]],'ranking':[{'company':k,'rows':v} for k,v in ranked]}
 out['validation']='Python Counter and independent SQLite GROUP BY match for all five groups'
 return out
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--input',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();out=run(a.input)
 a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'top5':{k:v['top5'] for k,v in out['groups'].items()},'totals':{k:v['total_rows'] for k,v in out['groups'].items()},'excluded':out['unmapped_sparten'],'validation':out['validation']},ensure_ascii=False))
