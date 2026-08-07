# Contributing to AMIE

## Workflow

1. Search existing issues.
2. Open an issue for substantial changes.
3. Discuss architecture before large implementations.
4. Create a focused branch.
5. Add tests and documentation.
6. Open a pull request.
7. Address review feedback.
8. Merge only after required checks pass.

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check .
```

## Design rule

Avoid coupling unrelated subsystems. Prefer small interfaces, dependency injection, explicit configuration, and observable behaviour.
