# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Run the interactive calculator:
```bash
python calculator.py
```

Run tests:
```bash
pytest test_calculator.py
```

Run a single test:
```bash
pytest test_calculator.py::test_divide
```

## Architecture

This is a minimal two-file Python project:

- **[calculator.py](calculator.py)** — four pure functions (`add`, `subtract`, `multiply`, `divide`) plus a `main()` REPL that parses free-form expressions like `3 + 4` and dispatches to them. `divide` raises `ValueError` on zero.
- **[test_calculator.py](test_calculator.py)** — pytest tests covering each function, including the divide-by-zero error path.

No external dependencies beyond `pytest`.
