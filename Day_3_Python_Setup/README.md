# Day 3: Python Project Setup

## Objective

To set up a proper Python project using virtual environment, project structure, and development tools.

---

## Tasks Performed

* Created a feature branch:
  git checkout -b feature/python-tooling

* Created virtual environment:
  python -m venv .venv

* Activated virtual environment

* Updated .gitignore to ignore .venv/

* Created project structure:
  src/my_project/

* Created Python file:
  app.py with basic function

* Created pyproject.toml for project configuration

* Installed tools:
  pip install ruff pre-commit

* Ran Ruff:
  ruff check .
  ruff format .

* Created pre-commit configuration file

* Installed pre-commit:
  pre-commit install

* Ran pre-commit:
  pre-commit run --all-files

---

## Why This is Important

Virtual environment keeps project dependencies separate.
pyproject.toml is used for managing project configuration.
Ruff helps in writing clean and error-free code.
Pre-commit ensures code quality automatically before every commit.

---

## What I Learned

I learned how to structure a Python project professionally.
I also learned how to use tools like Ruff and pre-commit to maintain code quality.

---

## Result

Successfully created a clean and professional Python project setup with automated code checking.
