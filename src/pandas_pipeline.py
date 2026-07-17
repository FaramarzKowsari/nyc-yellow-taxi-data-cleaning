
from __future__ import annotations
import argparse, json, time
from pathlib import Path
import numpy as np
import pandas as pd
import janitor  # registers clean_names
from cleaning_rules import *

DT_COLS=['tpep_pickup_datetime','tpep_dropoff_datetime']

def clean_pandas(df: pd.DataFrame):
    started=time.perf_counter(); before=len(df)
    df=df.clean_names().drop_duplicates().copy()
    for c in DT_COLS: df[c]=pd.to_datetime(df[c],errors='coerce')
    df['trip_duration_minutes']=(df.tpep_dropoff_datetime-df.tpep_pickup_datetime).dt.total_seconds()/60
    df['average_speed_mph']=np.where(df.trip_duration_minutes>0,df.trip_distance/(df.trip_duration_minutes/60),np.nan)
    month_ok=(df.tpep_pickup_datetime.dt.year.eq(PERIOD.year)&df.tpep_pickup_datetime.dt.month.eq(PERIOD.month))
    hard={
      'missing_timestamp':df[DT_COLS].isna().any(axis=1),
      'nonpositive_duration':df.trip_duration_minutes.le(0),
      'outside_analysis_month':~month_ok,
      'negative_distance':df.trip_distance.lt(0),
      'negative_passenger_count':df.passenger_count.lt(0),
      'invalid_pickup_zone':~df.pulocationid.between(ZONE_MIN,ZONE_MAX),
      'invalid_dropoff_zone':~df.dolocationid.between(ZONE_MIN,ZONE_MAX),
    }
    for n,s in hard.items(): df['rule_'+n]=s.fillna(True)
    soft={
      'zero_distance':df.trip_distance.eq(0),
      'long_duration':df.trip_duration_minutes.gt(MAX_DURATION_MINUTES),
      'high_speed':df.average_speed_mph.gt(MAX_REASONABLE_SPEED_MPH),
      'negative_fare':df.fare_amount.lt(0),
      'negative_total':df.total_amount.lt(0),
      'negative_tip':df.tip_amount.lt(0),
      'high_passenger_count':df.passenger_count.gt(6),
    }
    for n,s in soft.items(): df['flag_'+n]=s.fillna(False)
    df['is_hard_invalid']=df[[c for c in df if c.startswith('rule_')]].any(axis=1)
    df['is_suspicious']=df[[c for c in df if c.startswith('flag_')]].any(axis=1)
    cleaned=df.loc[~df.is_hard_invalid].copy()
    audit={'engine':'pandas+pyjanitor','rows_input':before,'duplicates_removed':before-len(df),'rows_after_dedup':len(df),'hard_invalid_rows':int(df.is_hard_invalid.sum()),'rows_output':len(cleaned),'suspicious_rows_retained':int(cleaned.is_suspicious.sum()),'runtime_seconds':round(time.perf_counter()-started,4)}
    return cleaned,df,audit

def main():
 p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',default='data/processed/yellow_taxi_cleaned_pandas.parquet');a=p.parse_args()
 df=pd.read_parquet(a.input); clean,classified,audit=clean_pandas(df);Path(a.output).parent.mkdir(parents=True,exist_ok=True);clean.to_parquet(a.output,index=False);Path(a.output+'.audit.json').write_text(json.dumps(audit,indent=2));print(json.dumps(audit,indent=2))
if __name__=='__main__':main()
