# Flask

## What is Flask?

Flask is a Python web framework. It listens for HTTP requests from the browser, decides what to do with each one, and sends back a response — usually an HTML page.

## What does Flask do in this app?

Flask handles all the server-side logic:

- receives GET and POST requests
- reads form data
- validates it
- queries the SQLite database
- renders templates and returns them as HTML

## Where is it in the project?

All Flask code is in `app.py`.

## Important ideas

### Routes

A route connects a URL to a Python function. When the browser requests that URL, Flask calls the function.

```python
@app.route("/")
def index():
    notes = get_db().execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
    return render_template("index.html", notes=notes)
```

### GET and POST

- **GET** — used when the browser is requesting a page to read.
- **POST** — used when the browser is submitting a form to change data.

```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # handle the submitted form
        ...
    return render_template("add.html", ...)
```

### Server-side validation

Flask checks that submitted data is valid before touching the database. If anything is missing, the form is shown again with an error message.

```python
if not form["title"] or not form["topic"] or not form["content"]:
    error = "Title, topic and content are all required."
```

### Redirecting after POST

After a successful insert or update, Flask redirects the browser back to the index page. This prevents the form being resubmitted if the user refreshes.

```python
return redirect(url_for("index"))
```

### 404 errors

The `get_note()` helper fetches a note by ID. If no note with that ID exists, Flask returns a 404 response automatically.

```python
def get_note(note_id):
    note = get_db().execute(
        "SELECT * FROM notes WHERE id = ?", (note_id,)
    ).fetchone()
    if note is None:
        abort(404)
    return note
```

### The database connection

Flask stores the database connection on `g`, a special object that lasts for one request. `get_db()` opens the connection the first time it is called and reuses it for the rest of that request. `close_db()` closes it at the end.

## Try changing this

Open `app.py` and find the `index` route. Change the SQL so notes are ordered oldest first:

```python
notes = get_db().execute(
    "SELECT id, title, topic, content FROM notes ORDER BY id ASC"
).fetchall()
```

Refresh the browser and check that the order changes.
