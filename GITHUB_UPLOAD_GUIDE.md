# GitHub Upload Guide

## Recommended repository name

`nyc-yellow-taxi-data-cleaning`

## Recommended description

Reproducible NYC Yellow Taxi data-cleaning pipelines using Pandas, PyJanitor, Polars, and DuckDB, with audit trails, automated tests, SQL validation, and documented anomaly rules.

## Recommended topics

`python`, `data-cleaning`, `data-engineering`, `pandas`, `polars`, `pyjanitor`, `duckdb`, `parquet`, `data-quality`, `nyc-taxi`, `open-data`, `jupyter-notebook`

## Upload with the GitHub web interface

1. Create a new public repository with the recommended name.
2. Do not initialize it with a README, license, or `.gitignore`; those files are already included.
3. Extract this ZIP archive locally.
4. Upload the contents of the `nyc-yellow-taxi-data-cleaning` folder, not the outer folder itself.
5. Commit the files to the default branch.
6. Enable GitHub Actions when prompted.
7. Add the recommended description and topics in the repository settings.

## Upload with Git

```bash
git init
git add .
git commit -m "Initial release: reproducible NYC taxi data-cleaning project"
git branch -M main
git remote add origin https://github.com/FaramarzKowsari/nyc-yellow-taxi-data-cleaning.git
git push -u origin main
```

## Recommended first release

Create a GitHub release tagged `v1.0.0` with the title:

`NYC Yellow Taxi Data Cleaning v1.0.0`

Suggested release summary:

> First stable release of a reproducible NYC Yellow Taxi data-cleaning project featuring equivalent Pandas/PyJanitor and Polars pipelines, DuckDB validation, deterministic tests, audit reports, notebooks, and open-source project governance files.

## Important data note

Do not upload the full raw monthly Parquet file to GitHub. The repository includes a downloader and records source metadata, while large raw and processed files are excluded through `.gitignore`.
