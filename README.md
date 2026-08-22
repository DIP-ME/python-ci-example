# Python CI Example

A tiny **Flask** app wired to a working **GitHub Actions** CI pipeline.
Push it to its own repo and the pipeline runs automatically.

## What's inside
```
app/calculator.py   # pure functions (add, divide)
app/web.py          # minimal Flask API (/health, /add, /divide)
tests/              # pytest tests for both
requirements.txt    # flask, pytest, ruff
pyproject.toml      # ruff + pytest config
.github/workflows/ci.yml
```

## The pipeline (`.github/workflows/ci.yml`)
Runs on every push to `main` and every pull request:
1. **Matrix** across Python 3.10 / 3.11 / 3.12
2. **Lint** with `ruff check`
3. **Format check** with `ruff format --check`
4. **Test** with `pytest`

Pip caching works because a `requirements.txt` is present (a missing
dependency file is the usual cause of the *"No file matched to
requirements.txt or pyproject.toml"* error from `setup-python`).

## Run it locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
ruff check . && ruff format --check .
pytest
python -m app.web        # serves http://localhost:5000/health
```

## Push to a new GitHub repo
```bash
git init
git add .
git commit -m "Python CI example"
git branch -M main
git remote add origin git@github.com:YOU/python-ci-example.git
git push -u origin main
```
Open the repo's **Actions** tab to watch it run.
