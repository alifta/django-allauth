# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django 6.0 authentication demo project featuring django-allauth integration with social login (Google, GitHub), user profiles, and a simple HTMX-powered todo application. The frontend uses Tailwind CSS with DaisyUI components.

**Key technologies:**
- Django 6.0 with Python 3.14+
- django-allauth for authentication (email/username login, social auth, optional MFA)
- django-htmx for dynamic UI interactions
- Tailwind CSS 3.4 + DaisyUI 4.12 for styling
- SQLite database (development)
- Bun for frontend tooling
- uv for Python dependency management
- Ruff for linting/formatting

## Development Setup

**Python dependencies:**
```sh
uv sync
```

**Frontend dependencies:**
```sh
bun install
```

**Database setup:**
```sh
uv run python manage.py makemigrations
uv run python manage.py migrate
```

**Run development server:**
```sh
uv run python manage.py runserver
```

**CSS development workflow:**
```sh
# Watch mode (development)
bun run watch-css

# Build minified CSS (production)
bun run build-css
```

## Testing & Quality

**Run tests:**
```sh
uv run python manage.py test
```

**Run specific test:**
```sh
uv run python manage.py test core.tests.TestClassName.test_method_name
```

**Linting and formatting (Ruff):**
```sh
# Check and auto-fix entire codebase
uv run ruff check --fix .
uv run ruff format .

# Fix specific file
uv run ruff check --fix --select I core/views.py  # Fix imports
uv run ruff format core/views.py
```

## Architecture

### Project Structure

- **config/**: Django settings, root URL configuration, WSGI/ASGI entry points
  - Settings module: `config.settings`
  - Root URLconf: `config.urls`

- **core/**: Main application containing authentication customization and todo features
  - Custom signup view (`CustomSignupView`) extends django-allauth with additional fields
  - User profile model (`UserProfile`) with phone, bio, birth_date fields
  - Todo model and HTMX-powered CRUD views

- **templates/**: Global templates
  - `base.html`: Base template with Tailwind/DaisyUI setup
  - `components/`: Reusable UI components

- **core/templates/core/**: App-specific templates
  - Uses django-template-partials for HTMX partial rendering
  - Todo views return partials using `#partial-name` syntax

- **static/**: Frontend assets
  - `css/input.css`: Tailwind input file
  - `css/main.css`: Compiled Tailwind output (gitignored in production workflows)

### Authentication Flow

1. **Standard login**: Email or username via django-allauth
2. **Social login**: Google and GitHub OAuth configured in `config/settings.py` (SOCIALACCOUNT_PROVIDERS)
3. **Signup customization**:
   - `core.forms.CustomSignupForm` adds first_name, last_name, phone, bio, birth_date
   - `core.views.CustomSignupView` extends allauth's SignupView
   - `UserProfile` model created automatically via form's `signup()` method
4. **Email verification**: Set to "optional" (development), configurable for "mandatory" (production)
5. **Redirects**:
   - Login → `core:secret` view
   - Signup/Logout → homepage

**MFA support**: Code includes commented-out MFA middleware and URLs - can be enabled by uncommenting and adding `allauth.mfa` to INSTALLED_APPS.

### URL Structure

- `/` - Homepage (core.views.index)
- `/about/` - About page
- `/secret/` - Protected page (login required)
- `/todo/` - Todo list (login required, HTMX)
- `/accounts/` - django-allauth authentication URLs
- `/admin/` - Django admin

### HTMX Integration

The todo application demonstrates HTMX patterns:
- Form submission returns partial HTML (`core/todo.html#todo-item-partial`)
- Uses `django-template-partials` for defining reusable fragments
- DELETE requests return 204 with `HX-Trigger` header for client-side updates
- Views use `@require_POST`, `@require_http_methods(["DELETE"])` decorators

### Frontend Styling

Tailwind config watches:
- `./templates/**/*.html`
- `./core/templates/**/*.html`
- `./**/*.html`
- `./static/js/**/*.js`

DaisyUI themes available (configured in tailwind.config.js). Default theme: 'light', dark mode: 'dark'.

## Common Patterns

**Adding a new protected view:**
```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return render(request, "core/my_template.html")
```

**Creating HTMX partial responses:**
```python
return render(request, "core/template.html#partial-name", context)
```

**User-specific queries:**
```python
MyModel.objects.filter(user=request.user)
```

**Email backend**: Configured to console output for development (`django.core.mail.backends.console.EmailBackend`). Change for production.

## Important Configuration Notes

- `SECRET_KEY` in settings.py is insecure - must be changed for production
- `DEBUG = True` - must be False in production
- Database: SQLite (development) - consider PostgreSQL for production
- Static files: Using STATICFILES_DIRS for development - run `collectstatic` for production
- Social auth requires API keys configured via Django admin or environment variables
