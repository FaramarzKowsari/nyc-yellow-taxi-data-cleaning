
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

DEFAULT_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet"

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024), b''): h.update(block)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--url',default=DEFAULT_URL)
    p.add_argument('--output',default='data/raw/yellow_tripdata_2025-01.parquet')
    a=p.parse_args(); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    req=Request(a.url,headers={'User-Agent':'Mozilla/5.0 nyc-taxi-data-cleaning/1.0'})
    with urlopen(req,timeout=120) as r, out.open('wb') as f:
        while chunk:=r.read(1024*1024): f.write(chunk)
    meta={'source_url':a.url,'downloaded_at_utc':datetime.now(timezone.utc).isoformat(),'bytes':out.stat().st_size,'sha256':sha256(out)}
    out.with_suffix(out.suffix+'.metadata.json').write_text(json.dumps(meta,indent=2))
    print(json.dumps(meta,indent=2))
if __name__=='__main__': main()
