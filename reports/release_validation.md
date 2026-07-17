# Release Validation

Release: `v1.0.0`

Validation date: 2026-07-17

## Automated checks

- Pytest result: 2 passed.
- Pandas/PyJanitor fixture pipeline: passed.
- Polars fixture pipeline: passed.
- DuckDB output validation: passed.
- Pandas and Polars audit metrics: equivalent.
- Hard-invalid records remaining in clean fixture output: 0.
- Non-positive trip durations remaining: 0.
- Invalid taxi zone IDs remaining: 0.
- Duplicate rows remaining: 0.

## Verified fixture metrics

| Metric | Value |
|---|---:|
| Input rows | 9 |
| Exact duplicates removed | 1 |
| Rows after deduplication | 8 |
| Hard-invalid rows removed | 4 |
| Final clean rows | 4 |
| Suspicious rows retained and flagged | 3 |

These metrics describe the committed deterministic fixture only. Full-month metrics must be generated locally from the official TLC Parquet source and must not be inferred from the fixture.
