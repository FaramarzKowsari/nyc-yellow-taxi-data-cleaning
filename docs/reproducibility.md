# Reproducibility

- Source URL is explicit and configurable.
- The downloader records SHA-256, byte size, and UTC download time.
- Dependencies are bounded in `requirements.txt`.
- Pipelines write a JSON audit trail.
- Pandas and Polars outputs can be compared by deterministic aggregate signatures.
- Tests run against a deliberately dirty fixture committed to the repository.
