
from __future__ import annotations
import argparse,json,time,re
from pathlib import Path
import polars as pl
from cleaning_rules import *

def snake(s):
 special={"VendorID":"vendorid","RatecodeID":"ratecodeid","PULocationID":"pulocationid","DOLocationID":"dolocationid","Airport_fee":"airport_fee"}
 if s in special: return special[s]
 return re.sub(r"(?<!^)(?=[A-Z])","_",s).lower()
def clean_polars(df:pl.DataFrame):
 started=time.perf_counter();before=df.height
 df=df.rename({c:snake(c) for c in df.columns}).unique(maintain_order=True)
 for c in ['tpep_pickup_datetime','tpep_dropoff_datetime']:
  if df.schema[c]==pl.String: df=df.with_columns(pl.col(c).str.to_datetime(strict=False))
 df=df.with_columns(((pl.col('tpep_dropoff_datetime')-pl.col('tpep_pickup_datetime')).dt.total_seconds()/60).alias('trip_duration_minutes'))
 df=df.with_columns(pl.when(pl.col('trip_duration_minutes')>0).then(pl.col('trip_distance')/(pl.col('trip_duration_minutes')/60)).otherwise(None).alias('average_speed_mph'))
 rules={
 'missing_timestamp':pl.any_horizontal(pl.col('tpep_pickup_datetime').is_null(),pl.col('tpep_dropoff_datetime').is_null()),
 'nonpositive_duration':pl.col('trip_duration_minutes')<=0,
 'outside_analysis_month':~((pl.col('tpep_pickup_datetime').dt.year()==PERIOD.year)&(pl.col('tpep_pickup_datetime').dt.month()==PERIOD.month)),
 'negative_distance':pl.col('trip_distance')<0,
 'negative_passenger_count':pl.col('passenger_count')<0,
 'invalid_pickup_zone':~pl.col('pulocationid').is_between(ZONE_MIN,ZONE_MAX),
 'invalid_dropoff_zone':~pl.col('dolocationid').is_between(ZONE_MIN,ZONE_MAX)}
 flags={'zero_distance':pl.col('trip_distance')==0,'long_duration':pl.col('trip_duration_minutes')>MAX_DURATION_MINUTES,'high_speed':pl.col('average_speed_mph')>MAX_REASONABLE_SPEED_MPH,'negative_fare':pl.col('fare_amount')<0,'negative_total':pl.col('total_amount')<0,'negative_tip':pl.col('tip_amount')<0,'high_passenger_count':pl.col('passenger_count')>6}
 df=df.with_columns([e.fill_null(True).alias('rule_'+n) for n,e in rules.items()]+[e.fill_null(False).alias('flag_'+n) for n,e in flags.items()])
 df=df.with_columns(pl.any_horizontal(pl.col('^rule_.*$')).alias('is_hard_invalid'),pl.any_horizontal(pl.col('^flag_.*$')).alias('is_suspicious'))
 clean=df.filter(~pl.col('is_hard_invalid'))
 audit={'engine':'polars','rows_input':before,'duplicates_removed':before-df.height,'rows_after_dedup':df.height,'hard_invalid_rows':df.select(pl.col('is_hard_invalid').sum()).item(),'rows_output':clean.height,'suspicious_rows_retained':clean.select(pl.col('is_suspicious').sum()).item(),'runtime_seconds':round(time.perf_counter()-started,4)}
 return clean,df,audit

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',default='data/processed/yellow_taxi_cleaned_polars.parquet');a=p.parse_args();df=pl.read_parquet(a.input);clean,classified,audit=clean_polars(df);Path(a.output).parent.mkdir(parents=True,exist_ok=True);clean.write_parquet(a.output);Path(a.output+'.audit.json').write_text(json.dumps(audit,indent=2));print(json.dumps(audit,indent=2))
if __name__=='__main__':main()
