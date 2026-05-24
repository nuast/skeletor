from pathlib import Path
import sqlite3

from flask import Flask, abort, g, redirect, render_template, request, url_for


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
app.config["DATABASE"] = BASE_DIR / "notes.db"


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    with sqlite3.connect(app.config["DATABASE"]) as connection:
        with open(BASE_DIR / "schema.sql") as schema_file:
            connection.executescript(schema_file.read())


@app.teardown_appcontext
def close_db(_error):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def get_note(note_id):
    note = get_db().execute(
        "SELECT id, title, topic, content FROM notes WHERE id = ?",
        (note_id,),
    ).fetchone()
    if note is None:
        abort(404)
    return note


@app.route("/")
def index():
    notes = get_db().execute(
        "SELECT id, title, topic, content FROM notes ORDER BY id DESC"
    ).fetchall()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = {"title": "", "topic": "", "content": ""}
    error = ""

    if request.method == "POST":
        form = {
            "title": request.form["title"].strip(),
            "topic": request.form["topic"].strip(),
            "content": request.form["content"].strip(),
        }

        if not form["title"] or not form["topic"] or not form["content"]:
            error = "Title, topic and content are all required."
        else:
            get_db().execute(
                "INSERT INTO notes (title, topic, content) VALUES (?, ?, ?)",
                (form["title"], form["topic"], form["content"]),
            )
            get_db().commit()
            return redirect(url_for("index"))

    return render_template("add.html", form=form, error=error)


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit(note_id):
    note = get_note(note_id)
    form = {
        "title": note["title"],
        "topic": note["topic"],
        "content": note["content"],
    }
    error = ""

    if request.method == "POST":
        form = {
            "title": request.form["title"].strip(),
            "topic": request.form["topic"].strip(),
            "content": request.form["content"].strip(),
        }

        if not form["title"] or not form["topic"] or not form["content"]:
            error = "Title, topic and content are all required."
        else:
            get_db().execute(
                "UPDATE notes SET title = ?, topic = ?, content = ? WHERE id = ?",
                (form["title"], form["topic"], form["content"], note_id),
            )
            get_db().commit()
            return redirect(url_for("index"))

    return render_template("edit.html", note=note, form=form, error=error)


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    get_db().execute("DELETE FROM notes WHERE id = ?", (note_id,))
    get_db().commit()
    return redirect(url_for("index"))


@app.cli.command("init-db")
def init_db_command():
    init_db()
    print("Database initialised.")


if not app.config["DATABASE"].exists():
    init_db()


if __name__ == "__main__":
    app.run()
