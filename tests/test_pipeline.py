
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
import pandas as pd, polars as pl
from generate_sample import build_sample
from pandas_pipeline import clean_pandas
from polars_pipeline import clean_polars

def test_pipeline_equivalence():
 df=build_sample(); p,_,pa=clean_pandas(df); q,_,qa=clean_polars(pl.from_pandas(df))
 assert pa['rows_input']==qa['rows_input']==9
 assert pa['duplicates_removed']==qa['duplicates_removed']==1
 assert pa['rows_output']==qa['rows_output']==4
 assert pa['hard_invalid_rows']==qa['hard_invalid_rows']==4
 assert int(p.is_suspicious.sum())==q.select(pl.col('is_suspicious').sum()).item()==3

def test_hard_constraints():
 df=build_sample(); clean,_,_=clean_pandas(df)
 assert (clean.trip_duration_minutes>0).all()
 assert clean.pulocationid.between(1,265).all()
 assert clean.dolocationid.between(1,265).all()
 assert (clean.trip_distance>=0).all()
