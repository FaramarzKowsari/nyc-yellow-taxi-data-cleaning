# Contributing

Thank you for considering a contribution to this project.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Contribution workflow

1. Fork the repository and create a focused branch.
2. Keep changes small, documented, and reproducible.
3. Add or update tests for every behavioral change.
4. Run the full test suite before opening a pull request.
5. Explain data-quality implications in the pull request description.

## Coding standards

- Use clear, descriptive names and type hints where practical.
- Keep cleaning rules centralized in `src/cleaning_rules.py`.
- Do not silently delete suspicious observations; flag them unless a documented hard rule is violated.
- Do not commit large raw or generated datasets.
- Keep notebooks deterministic and free of hidden state.

## Reporting data issues

When proposing a new cleaning rule, include:

- the affected field;
- a reproducible example;
- evidence from the official TLC schema or domain logic;
- the expected classification: valid, suspicious, or invalid;
- the expected effect on row counts.
