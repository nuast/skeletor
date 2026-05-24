# skeletor

This project is a tiny full-stack Flask app for OCR A-Level Computer Science students. It uses HTML forms, Jinja templates, Flask routes, JavaScript, and SQLite to create, read, update, and delete notes.

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
- `/static/img/logo.png` - logo image file requested by the browser on each page
- `/templates/base.html` - shared page layout used by all templates
- `/templates/index.html` - shows notes read from the database
- `/templates/add.html` - form for inserting a new note
- `/templates/edit.html` - form for updating an existing note
- `/README.md` - setup instructions and concept mapping

## JavaScript in `static/script.js`

Students should use `script.js` to learn these browser-side ideas:

- selecting elements from the DOM with `document.querySelectorAll()`
- looping through matching elements with a `for...of` loop
- adding an event listener with `addEventListener()`
- handling a `submit` event from a form
- using `window.confirm()` to ask the user to confirm an action
- using `event.preventDefault()` to stop the browser sending a form
- understanding that JavaScript runs in the browser, while Flask runs on the server
- understanding that client-side behaviour can improve usability, but server-side validation is still essential

The script only confirms deletions. It does not replace Flask validation and it does not add extra interface features.

## CSS in `static/style.css`

Students should use `style.css` to identify these CSS ideas:

- **element selectors** such as `body`, `label`, `input`, and `textarea`
- **class selectors** such as `.page`, `.button`, `.card`, and `.note-form`
- **grouped selectors** such as `h1, h2, p` and `.button, button`
- **colour and presentation properties** including `color` and `background-color`
- **text styling properties** including `font-family` and `font-size`
- **box model properties** including `width`, `height`, `padding`, `margin`, and `max-width`
- **border properties** including `border-style`, `border-width`, and `border-color`

CSS is separated from HTML so that the HTML can describe the structure and content of the page, while the CSS controls how that content is presented in the browser.

This means the appearance of the page can be changed without changing the actual text, form fields, links, or page structure.

The stylesheet in this project is deliberately simple so students can match visible parts of the interface to the CSS rules that control them.

## Static assets and the logo

- Static assets are files such as CSS, JavaScript, and images that are sent to the browser as files instead of being rendered as templates.
- Images belong in `/static` so they can be requested directly by URL (for example `/static/img/logo.png`).
- Flask serves files in the `static` folder automatically, so templates can link to them with `url_for('static', filename='...')`.
- The logo is rendered in `templates/base.html` with `<img src="{{ url_for('static', filename='img/logo.png') }}">`, so it appears on every page that extends `base.html`.

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
