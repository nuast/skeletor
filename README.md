# skeletor

This project is a tiny full-stack Flask app for OCR A-Level Computer Science students. It uses HTML forms, Jinja templates, Flask routes, JavaScript, and SQLite to create, read, update, and delete revision notes.

## Install Flask

```bash
pip install flask
```

## Initialise the database

The app can create `notes.db` automatically on first run, or you can initialise it yourself from `schema.sql`:

```bash
python -c "from app import init_db; init_db()"
```

## Run the app

```bash
python app.py
```

Then open `http://127.0.0.1:5000`.

## What each file is for

- `/app.py` - Flask routes, form handling, validation, SQLite queries, and database setup
- `/schema.sql` - SQL to create the single `notes` table
- `/static/style.css` - simple page styling
- `/static/script.js` - small client-side JavaScript to confirm deletes
- `/static/img/logo.png` - site logo served as a static file
- `/templates/base.html` - shared page layout used by all templates
- `/templates/index.html` - shows notes read from the database
- `/templates/add.html` - form for inserting a new note
- `/templates/edit.html` - form for updating an existing note
- `/README.md` - setup instructions and concept mapping

## Static assets

Static assets are files that Flask serves exactly as they are — images, CSS, and JavaScript — without any Python processing.

Flask keeps static assets in the `/static/` folder so they are clearly separated from the Jinja templates in `/templates/`. Templates contain Python logic and dynamic content; static files contain fixed content that every browser can cache.

When a browser loads a page it sends one HTTP GET request for the HTML, then separate HTTP GET requests for every linked asset (CSS, JS, images). Flask handles each of these requests automatically for anything inside `/static/`.

### How the logo is rendered

`base.html` uses `url_for('static', filename='img/logo.png')` to build the correct URL for the image:

```html
<img src="{{ url_for('static', filename='img/logo.png') }}" alt="Skeletor logo" class="logo">
```

`url_for` is a Flask helper that generates the right URL regardless of where the app is hosted. The browser then requests `/static/img/logo.png` and Flask returns the file. Because `base.html` is the parent template, the logo appears on every page automatically through Jinja template inheritance.

## OCR A-Level Computer Science links

- **Browser**: displays the HTML, CSS, and JavaScript
- **HTTP GET**: used when requesting pages such as `/` and `/add`
- **HTTP POST**: used when submitting add, edit, and delete forms
- **Flask routes**: receive requests and choose what should happen next
- **Jinja templates**: turn Python data into HTML pages
- **SQLite**: stores the revision notes in a table
- **CRUD**: create, read, update, and delete notes through the web interface

## What the app demonstrates

- routing
- GET and POST requests
- form handling
- server-side validation
- template inheritance
- parameterised SQL queries
- database-driven page rendering
