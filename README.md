# Expense Tracker CLI

A lightweight, object-oriented Command Line Interface (CLI) application built with Python to track daily incomes, expenses, and current balances. The application stores data locally in a JSON database and features formatted console tables using the `rich` library.

## 🚀 Features

- Log Expenses & Incomes with structural validation via OOP models.
- Persistent local storage inside a JSON file.
- Interactive views with automated financial balance summaries in stylized tables.
- Update or delete specific records by targeting their history index.
- Robust error handling to protect inputs against empty strings or improper data types.
- Unit testing suite via `pytest`.

## project Structure

```text
EXPENSE_TRACKER/
│
├── .pytest_cache/
├── .venv/
│
├── Data/
│   └── db.json
│
├── Src/
│   ├── __init__.py
│   ├── app.py
│   ├── models.py
│   └── storage.py
│
├── Tests/
│   ├── __init__.py
│   └── test_tracker.py
│
├── .gitignore
├── Pipfile
├── Pipfile.lock
└── README.md
```
