# Student Records Management System

Simple Python-based student records management project used for college hands-on exercises.

## Description

This project lets you add, view, update, and delete student records using simple Python scripts and an SQLite database.

## Prerequisites

- Python 3.8+ (SQLite is included with the standard library)

## Quick start

1. (Optional) Create a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Run the main script (this project contains multiple entry points — use the one you developed):

   ```powershell
   python CRUDoperations.py
   ```

3. Alternatively run the UI/flow you prefer:

   - `login.py`
   - `addStudent.py`
   - `dashboard.py`

## Files

- `CRUDoperations.py` - Core create/read/update/delete operations
- `Database.py` - Database connection and helpers
- `addStudent.py` - Script to add a student
- `login.py` - Login flow for the app
- `dashboard.py` - Dashboard UI script
- `graph.py` - Generates graphs (optional)
- `students_data.csv` - Sample CSV data
- `students.db` - Local SQLite database (ignored by `.gitignore`)

## Notes

- No external dependencies are required unless you added plotting or GUI libraries.
- `students.db` is ignored by git; if you want to include a seed DB, remove it from `.gitignore` first.

## License

This repository has no license file. Add one if you want to open-source the code (e.g., MIT).
