# Copilot / AI Agent Instructions — EstudaPlus
```markdown
# Copilot / AI Agent Instructions — EstudaPlus (concise)

Purpose: give AI agents the precise, actionable context required to make safe, correct changes in this repository.

- **Big picture / architecture:**
  - Backend: Django 5.2.1 + Django REST Framework. Frontend is a separate Next.js app (see `EstudaPlus/README.md`).
  - Apps in this repo: `accounts` (custom `User` model and auth endpoints) and `courses` (courses, modules, lessons, enrollment, reviews).
  - Routes: `core/urls.py` mounts `api/v1/accounts/` and `api/v1/courses/`.

- **Critical files & behavior to preserve:**
  - `core/settings.py`: reads secrets via `python-decouple` (`config('DJANGO_SECRET_KEY')`) and configures MySQL DB using env vars.
  - `AUTH_USER_MODEL = 'accounts.User'` (do not replace without careful migration strategy).
  - DRF defaults in `core/settings.py`:
    - `EXCEPTION_HANDLER` → `core.utils.custom_exception.custom_exception_handler`
    - `DEFAULT_RENDERER_CLASSES` → `core.utils.renderers.CustomJSONRenderer` (wraps all responses in `{success,data}`)
    - `DEFAULT_AUTHENTICATION_CLASSES` → JWT (`rest_framework_simplejwt`)
    - `DEFAULT_PERMISSION_CLASSES` → `IsAuthenticated` (public endpoints use `AllowAny` explicitly)
  - `core/utils/` contains the project's error-handling and renderer conventions: `custom_exception.py`, `renderers.py`, `exceptions.py`, `formatters.py`.

- **Common developer workflows (exact commands):**
  - Create venv: `python -m venv .venv`
  - Activate (PowerShell): `.\.venv\Scripts\Activate.ps1`
  - Install deps: `pip install -r requirements.txt`
  - Required env vars in `.env`: `DJANGO_SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.
  - Run migrations: `python manage.py migrate`
  - Run server: `python manage.py runserver`
  - Create superuser: `python manage.py createsuperuser`
  - Run tests: `python manage.py test`
  - SQL backup: `cursos_backup.sql` exists at repo root — use it to restore course data if needed.

- **Project-specific conventions & gotchas:**
  - `APPEND_SLASH = False` — endpoints are strict about trailing slashes.
  - Responses are normalized by `CustomJSONRenderer`; return DRF `Response` objects and let the renderer wrap them.
  - Validation errors should be raised as `core.utils.exceptions.ValidationError(format_serializer_error(serializer.errors))` to match existing clients.
  - Many course-related flows rely on `Enrollment`, `WatchedLesson` and `Review` checks; see `courses/views.py` for patterns (e.g., `submit_review` and `content` actions).
  - DB is MySQL by default per `settings.py` and `README.md` — do not assume SQLite unless you intentionally switch configs for local dev.

- **Where to look when changing behavior:**
  - `core/settings.py` — environment and DRF defaults.
  - `accounts/views.py` — sign in/up semantics, token creation, password hashing.
  - `courses/views.py` — read-only viewset, custom actions (`reviews`, `submit_review`, `content`) and lesson-watched endpoints.
  - `core/utils/` — rendering and exception handling.

If you want this trimmed into a one-page checklist (for PR reviewers or junior contributors), I can produce that next. Please tell me which area to shorten or expand.

```
