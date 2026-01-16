# Home in Block

## Project Setup

Install `uv` (if not already installed):

```sh
brew install uv
```

Creates virtual environment and installs or sync dependency packages:

```sh
uv sync
```

This will:

- Create a virtual environment (if it doesn't exist)
- Install all dependencies from `pyproject.toml`
- Use Python 3.14+ (automatically downloaded if needed)

Activate the virtual environment (optional, but recommended for interactive use):

```sh
source .venv/bin/activate
```

Note: If virtual environment is activated, you can run commands normally, but you can also run commands directly with `uv run` without activating the environment:

```sh
python manage.py runserver
# OR
uv run python manage.py runserver
```

Note: You can also run commands directly with `uv run` without activating the environment.

## Managing Dependencies

Add a new dependency:

```sh
uv add <package-name>
```

Add a development dependency:

```sh
uv add --group dev <package-name>
```

Remove a dependency:

```sh
uv remove <package-name>
```

### Updating Dependencies

Update all dependencies and dev dependencies to latest compatible versions:

```sh
uv lock --upgrade          # Update lockfile to latest compatible versions
uv sync --group dev        # Sync dependencies including dev group
```

Update individual packages:

```sh
uv add --upgrade <package-name>              # Update specific package
uv add --upgrade --group dev <package-name>  # Update dev dependency
```

**Note**: Your `pyproject.toml` uses minimum version constraints (e.g., `Django>=6.0`). The `uv.lock` file pins exact versions. When you run `uv lock --upgrade`, it updates the lockfile to the latest compatible versions within your constraints.

## Django Commands

All Django commands should be prefixed with `uv run`:

Run development server:

```sh
uv run python manage.py runserver
```

Create superuser:

```sh
uv run python manage.py createsuperuser
```

Run Django shell:

```sh
uv run python manage.py shell
```

## Database Commands

Run migrations:

```sh
uv run python manage.py migrate
```

Create migrations:

```sh
uv run python manage.py makemigrations
```

## UI

First setup (install dependencies):

```sh
bun install
```

Dependencies management:

```sh
bun add <package>
bun remove <package>
```

Build CSS (production):

```sh
bun run build-css
```

Watch and rebuild CSS (development):

```sh
bun run watch-css
```

## Linting

Install Ruff:

```sh
uv add --dev ruff
uv sync --extra dev
```

Lint and auto-fix import sorting issues for a specific file:

```sh
uv run ruff check --fix --select I directory/file.py
```

Format the code for a specific file:

```sh
uv run ruff format directory/file.py
```

Format all Python files:

```sh
uv run ruff check --fix .
uv run ruff format .
```

## Django Template Formatting

This project uses **DjLint** for formatting Django templates. DjLint properly handles Django template tags and ensures each tag is on its own line.

Format a specific template file:

```sh
uv run djlint --reformat path/to/template.html
```

Format all templates in a directory:

```sh
uv run djlint --reformat core/templates/
```

Format all templates in the project:

```sh
uv run djlint --reformat templates/ core/templates/
```

Check formatting without making changes:

```sh
uv run djlint --check templates/ core/templates/
```

**Note**: DjLint is configured in `pyproject.toml` and will automatically format Django template tags, HTMX attributes, and HTML content.
