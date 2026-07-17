PYTHON ?= python
DATA_URL ?= https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet

install:
	$(PYTHON) -m pip install -r requirements.txt

download:
	$(PYTHON) src/download_data.py --url $(DATA_URL)

sample:
	$(PYTHON) src/generate_sample.py

clean-pandas:
	$(PYTHON) src/pandas_pipeline.py --input data/raw/yellow_tripdata_2025-01.parquet

clean-polars:
	$(PYTHON) src/polars_pipeline.py --input data/raw/yellow_tripdata_2025-01.parquet

validate:
	$(PYTHON) src/duckdb_validation.py --input data/processed/yellow_taxi_cleaned_polars.parquet

test:
	pytest -q

all: download clean-polars validate test
