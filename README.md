# Home in Block

## Database

Run migrations:

```sh
uv run python manage.py makemigrations
uv run python manage.py migrate
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
