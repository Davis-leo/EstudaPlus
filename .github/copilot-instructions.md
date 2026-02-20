# Copilot / AI Agent Instructions — EstudaPlus

Purpose: Help AI coding agents become immediately productive in this Django repository.

- **Big picture:** This is a minimal Django project (`core`) generated with Django 5.2.1 and configured for a small REST API surface (DRF is installed). The database is SQLite (`db.sqlite3`) at the repo root and the admin site is mounted at `/admin/`.

- **Key files:**
  - [core/settings.py](core/settings.py) — central config (INSTALLED_APPS includes `rest_framework`; `SECRET_KEY` is currently in-file but `python-decouple` is imported).
  - [manage.py](manage.py) — canonical entrypoint for running tasks, migrations, and server.
  - [core/urls.py](core/urls.py) — project URL root (add `include()` here for app routes).
  - `/db.sqlite3` — local SQLite DB (committed in repo currently).

- **Developer workflows (commands):**
  - Create venv: `python -m venv .venv`
  - Activate (PowerShell): `.\\.venv\\Scripts\\Activate.ps1` or (cmd): `.venv\\Scripts\\activate`
  - Install deps: `pip install -r requirements.txt` (if missing) or `pip install django djangorestframework python-decouple`
  - Apply migrations: `python manage.py migrate`
  - Run development server: `python manage.py runserver`
  - Create superuser: `python manage.py createsuperuser`
  - Run tests: `python manage.py test`

- **Project-specific conventions / patterns:**
  - Add new Django apps at the repository root and register them in `INSTALLED_APPS` in [core/settings.py](core/settings.py).
  - Expose app endpoints by `include()`-ing their `urls.py` from [core/urls.py](core/urls.py); e.g. add `path('api/', include('myapp.urls'))`.
  - `python-decouple` is present in `settings.py` but not yet used for `SECRET_KEY` or environment overrides — prefer a `.env` file for secrets and set `SECRET_KEY`, `DEBUG`, and DB overrides there.
  - Templates: `TEMPLATES['DIRS']` is empty; put HTML templates under `your_app/templates/`.
  - Static files served via `STATIC_URL = 'static/'` — collect/static workflow not configured; keep static assets in `static/` within apps for dev.

- **Integration points & external deps:**
  - Django core (project created with Django 5.2.1). Use the Django management CLI for most tasks.
  - Django REST Framework (`rest_framework`) is already in `INSTALLED_APPS` — use DRF viewsets/serializers for APIs.
  - `python-decouple` indicates environment-driven config is intended; add `.env` and avoid committing secrets.

- **Conventions that differ from defaults / gotchas:**
  - `db.sqlite3` is present in repo root; be cautious — tests/dev will reuse this DB unless you configure an alternate DB or ephemeral test DB.
  - `SECRET_KEY` is hard-coded in `settings.py` currently. Move it to `.env` and load with `config('SECRET_KEY')` to avoid leaking secrets.
  - `DEBUG = True` — production hardening is not yet configured.

- **Examples for common edits:**
  - Register an app: add `'myapp',` to `INSTALLED_APPS` in [core/settings.py](core/settings.py).
  - Expose app routes: in [core/urls.py](core/urls.py) add `from django.urls import include, path` and `path('api/', include('myapp.urls'))`.

If any of these sections are unclear or you'd like more detail (example `.env`, requirements file, or a short RFC for migrating secrets), tell me which part to expand and I'll iterate.
