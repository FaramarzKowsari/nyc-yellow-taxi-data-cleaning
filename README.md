
# NYC Yellow Taxi Data Cleaning: Pandas, Polars, PyJanitor and DuckDB

A production-oriented, reproducible, and audit-friendly data-cleaning project built on the official New York City Taxi & Limousine Commission (TLC) Yellow Taxi Trip Records.

## Overview

This repository demonstrates how to design, test, compare, and independently validate a transparent data-cleaning workflow for a large public transportation dataset. It is intended as a portfolio-quality data engineering project and as a reusable reference implementation.

## Project goals

- clean a real, large public dataset with explicit rules;
- distinguish **invalid** observations from merely **suspicious** ones;
- implement equivalent pipelines in Pandas/PyJanitor and Polars;
- validate the final Parquet independently with DuckDB SQL;
- preserve an audit trail suitable for technical review.

## Official sources

- TLC Trip Record Data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- Yellow Taxi Data Dictionary: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
- Default file: January 2025 Yellow Taxi Trip Records
- Direct Parquet URL: https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-01.parquet

TLC notes that trip records are supplied by technology providers and may contain inaccuracies. This repository therefore documents every cleaning decision and avoids treating all outliers as errors.

## Repository map

```text
src/       production-style pipelines and downloader
notebooks/ guided, executable walkthroughs
tests/     deterministic tests using a committed dirty fixture
sql/       independent DuckDB validation queries
docs/      methodology, limitations and reproducibility notes
reports/   generated audit and validation outputs
data/      sample data plus ignored raw/processed directories
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/download_data.py
python src/polars_pipeline.py --input data/raw/yellow_tripdata_2025-01.parquet
python src/duckdb_validation.py --input data/processed/yellow_taxi_cleaned_polars.parquet
pytest -q
```

## Cleaning policy

Hard-invalid records are excluded from the final clean table. Suspicious but logically possible records are retained with flags. See `docs/methodology.md` for the full rationale.

### Hard rules

- valid pickup and drop-off timestamps;
- positive trip duration;
- pickup inside January 2025 for the default analysis;
- non-negative trip distance and passenger count;
- pickup and drop-off location IDs within 1-265.

### Soft flags

- zero distance;
- duration above four hours;
- average speed above 80 mph;
- negative fare, total or tip;
- passenger count above six.

## Verified fixture result

The committed dirty fixture contains nine rows, including one duplicate. Both implementations produce the same audit result:

| Metric | Result |
|---|---:|
| Input rows | 9 |
| Exact duplicates removed | 1 |
| Hard-invalid rows | 4 |
| Final rows | 4 |
| Suspicious rows retained | 3 |

These numbers refer only to the test fixture, not to the complete TLC month. Full-month results are generated locally from the official source file and written to JSON audit files.

## Why four tools?

- **Pandas** provides a familiar baseline.
- **PyJanitor** improves naming and method-chain readability.
- **Polars** provides a modern, parallel columnar implementation.
- **DuckDB** performs independent SQL validation directly against Parquet.

## Reproducibility and data size

The large source and generated Parquet files are intentionally ignored by Git. The repository includes the official URL, a downloader that records SHA-256 metadata, deterministic tests, and a small dirty fixture. This is more reproducible than committing an opaque large binary.

## Repository topics

`data-cleaning` `data-engineering` `pandas` `polars` `pyjanitor` `duckdb` `parquet` `data-quality` `nyc-taxi` `python`

## Contributing

Contributions are welcome. Read `CONTRIBUTING.md`, follow the documented data-quality policy, and use the issue and pull-request templates.

## Citation

Citation metadata is provided in `CITATION.cff`.

## Author

Faramarz Kowsari

## License

Code: MIT. Data: consult the NYC TLC source portal and NYC Open Data terms.
