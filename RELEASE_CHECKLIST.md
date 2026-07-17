# Release Checklist

- [ ] Run `pytest -q`.
- [ ] Run both cleaning pipelines on the committed fixture.
- [ ] Confirm DuckDB validation succeeds.
- [ ] Confirm notebooks run from a fresh kernel.
- [ ] Review generated audit reports for unexpected row-count changes.
- [ ] Update `CHANGELOG.md`.
- [ ] Update the version in `pyproject.toml` and `CITATION.cff`.
- [ ] Confirm no raw full-month dataset or credentials are tracked.
- [ ] Create a signed Git tag and GitHub release.
