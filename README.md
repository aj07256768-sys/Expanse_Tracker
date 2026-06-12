# Simple Expense Tracker

A lightweight, terminal-based command-line application built with Python to help you easily monitor your daily financial habits by tracking expenses and income.

---

## 📁 Project Structure

The project is modularly organized into distinct folders and files to ensure clean code separation, high maintainability, and scalability:

```text
EXPENSE_TRACKER/
│
├── Data/
│   └── db.json          # Local JSON database storing your transactions
│
├── Src/
│   ├── __init__.py      # Makes Src a recognizable Python package
│   ├── app.py           # Application entry point and CLI command logic
│   ├── models.py        # Business logic definitions (Expense/Income classes)
│   ├── storage.py       # Functions to handle reading and writing to db.json
│   └── utils.py         # Helper functions (date formatting, calculations)
│
├── Tests/
│   ├── __init__.py      # Makes Tests a recognizable Python package
│   └── test_tracker.py  # Unit tests to ensure core logic runs flawlessly
│
├── .gitignore           # Prevents system files and caches from being tracked
├── Pipfile              # Defines project dependencies for Pipenv
└── Pipfile.lock         # Locks exact dependency versions for stability
```
