# Full-month results pending local source download

The execution environment used to assemble this repository could not download the 58+ MB CloudFront source file. No full-month statistics are fabricated here.

Run:

```bash
python src/download_data.py
python src/pandas_pipeline.py --input data/raw/yellow_tripdata_2025-01.parquet
python src/polars_pipeline.py --input data/raw/yellow_tripdata_2025-01.parquet
python src/duckdb_validation.py --input data/processed/yellow_taxi_cleaned_polars.parquet
```

The pipelines then create reproducible JSON audit outputs from the official file.
