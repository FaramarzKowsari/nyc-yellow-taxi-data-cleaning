# Verified sample audit report

This report is generated from the committed, deliberately dirty nine-row fixture. It is not presented as a full-month TLC result.

## Pandas + PyJanitor

```json
{
  "engine": "pandas+pyjanitor",
  "rows_input": 9,
  "duplicates_removed": 1,
  "rows_after_dedup": 8,
  "hard_invalid_rows": 4,
  "rows_output": 4,
  "suspicious_rows_retained": 3,
  "runtime_seconds": 0.0319
}
```

## Polars

```json
{
  "engine": "polars",
  "rows_input": 9,
  "duplicates_removed": 1,
  "rows_after_dedup": 8,
  "hard_invalid_rows": 4,
  "rows_output": 4,
  "suspicious_rows_retained": 3,
  "runtime_seconds": 0.0779
}
```

## DuckDB validation

```json
{
  "row_count": 4,
  "hard_invalid_rows": 0,
  "nonpositive_duration": 0,
  "invalid_zones": 0,
  "duplicate_rows": 0,
  "suspicious_rows": 3,
  "passed": true
}
```

## Conclusion

Both cleaning engines agree on all core audit counts. DuckDB confirms that no hard-invalid row, non-positive duration, invalid zone, or exact duplicate survives in the sample output.
