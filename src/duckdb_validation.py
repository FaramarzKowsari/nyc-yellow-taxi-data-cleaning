
from __future__ import annotations
import argparse,json
from pathlib import Path
import duckdb

def validate(path):
 con=duckdb.connect(); safe=str(path).replace("'", "''"); con.execute(f"CREATE VIEW cleaned AS SELECT * FROM read_parquet('{safe}')")
 checks={
 'row_count':'SELECT COUNT(*) FROM cleaned',
 'hard_invalid_rows':'SELECT COUNT(*) FROM cleaned WHERE is_hard_invalid',
 'nonpositive_duration':'SELECT COUNT(*) FROM cleaned WHERE trip_duration_minutes <= 0',
 'invalid_zones':'SELECT COUNT(*) FROM cleaned WHERE pulocationid NOT BETWEEN 1 AND 265 OR dolocationid NOT BETWEEN 1 AND 265',
 'duplicate_rows':'SELECT COUNT(*) - (SELECT COUNT(*) FROM (SELECT DISTINCT * FROM cleaned)) FROM cleaned',
 'suspicious_rows':'SELECT COUNT(*) FROM cleaned WHERE is_suspicious'}
 out={k:con.execute(q).fetchone()[0] for k,q in checks.items()};out['passed']=all(out[k]==0 for k in ['hard_invalid_rows','nonpositive_duration','invalid_zones','duplicate_rows']);return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);a=p.parse_args();out=validate(a.input);Path('reports').mkdir(exist_ok=True);Path('reports/duckdb_validation.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
if __name__=='__main__':main()
