# Copilot Instructions

## Project overview

Skeletor is a deliberately minimal Flask CRUD app for OCR A-Level Computer Science students. Its purpose is to demonstrate routing, GET/POST, form handling, server-side validation, template inheritance, parameterised SQL, and SQLite — one concept per file. Keep changes simple and teachable.

## Running the app

```bash
pip install flask          # install dependency
python app.py              # run on http://127.0.0.1:5000
```

Initialise the database manually (auto-runs on first start if `notes.db` is absent):

```bash
python -c "from app import init_db; init_db()"
```

## Architecture

Everything lives in `app.py`: Flask app setup, DB helpers, and all route handlers. There is one table (`notes`) defined in `schema.sql`.

```
app.py          – all routes, form validation, SQLite queries, DB lifecycle
schema.sql      – CREATE TABLE for notes (id, title, topic, content)
templates/
  base.html     – shared layout; all other templates extend this
  index.html    – lists all notes (GET /)
  add.html      – create form (GET/POST /add)
  edit.html     – edit form (GET/POST /edit/<id>)
static/
  style.css     – page styling
  script.js     – delete-confirmation only; no other client-side logic
```

## Key conventions

- **Raw SQL, no ORM.** All queries use parameterised placeholders (`?`) directly via `sqlite3`.
- **DB connection via Flask `g`.** `get_db()` opens and caches the connection on `g`; `close_db()` is registered with `@app.teardown_appcontext`. Never open a connection outside this pattern.
- **Validation in the route, not a form library.** Each POST handler strips whitespace, checks all fields are non-empty, and re-renders the template with the form data and an `error` string on failure.
- **`get_note(note_id)` is a shared helper** that fetches a note by ID and calls `abort(404)` if missing. Use it in any route that takes a `note_id`.
- **Template inheritance.** All page templates use `{% extends "base.html" %}` and fill `{% block content %}`. The base template includes the stylesheet and `script.js`.
- **`url_for` everywhere.** Static assets and links always use `url_for('static', filename='...')` and `url_for('<route_name>')` — never hardcoded paths.
- **Delete uses POST.** The delete action is a `<form method="post">` (not a link), confirmed client-side by `script.js` before submission.
