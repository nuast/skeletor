# Skeletor

A bare-bones full-stack web app skeleton for OCR A-Level Computer Science students.

It uses **HTML**, **CSS**, **JavaScript**, **Flask**, **Jinja**, and **SQLite** to build a working notes app where you can create, read, update, and delete records through a browser.

---

## What you will learn

This app shows how a simple full-stack web app connects all its parts:

| Layer | Technology |
|---|---|
| Browser | HTML pages |
| Presentation | CSS styling |
| Client-side behaviour | JavaScript |
| Server-side logic | Flask routes |
| Dynamic pages | Jinja templates |
| Data storage | SQLite database |

---

## 1. Fork the repository

Forking creates your own copy of the project on GitHub so your changes are separate from the teacher's original.

1. Sign in to [github.com](https://github.com).
2. Open the repository page.
3. Click the **Fork** button near the top right.
4. Keep the default settings and click **Create fork**.

You now have your own copy at `https://github.com/YOUR-USERNAME/skeletor`. Changes you make here will not affect the original.

---

## 2. Create a GitHub projects folder

Before cloning, create a dedicated folder on your computer where all your GitHub repositories will live. A good location is:

```
Documents/GitHub
```

Keeping all repositories in one place makes them easy to find and manage.

---

## 3. Clone the repository

Cloning downloads your fork to your computer. Open a terminal and run:

```bash
cd Documents/GitHub
git clone https://github.com/YOUR-USERNAME/skeletor.git
```

Replace `YOUR-USERNAME` with your GitHub username.

`git clone` creates the `skeletor` folder automatically — do not create it yourself first.

---

## 4. Open the project in VS Code

Open VS Code from the `GitHub` folder rather than navigating into the project first:

```bash
cd Documents/GitHub
code skeletor
```

This is the cleanest approach and avoids unnecessary directory changes.

> **School machines:** If the `code` command is blocked, open VS Code manually, choose **File → Open Folder**, and select the `skeletor` folder.

---

## 5. Create a Python virtual environment

A virtual environment is a private copy of Python for this project. Packages you install here will not affect other projects.

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

When the virtual environment is active, your terminal prompt will start with `(.venv)`.

---

## 6. Install requirements

```bash
pip install -r requirements.txt
```

This installs Flask and any other packages the app needs.

---

## 7. Initialise the database

The database is created automatically the first time you run the app. To reset it at any point, run:

```bash
flask --app app init-db
```

This recreates the `notes` table using `schema.sql`.

---

## 8. Run the app

```bash
python app.py
```

Then open the URL shown in the terminal — usually:

```
http://127.0.0.1:5000
```

---

## 9. Make your first change

Try one of these to get started:

- **Change the site title** — open `templates/base.html` and edit the `<h1>` tag.
- **Change a colour** — open `static/style.css` and change `background-color: #f5f7fb` on the `body` rule.
- **Add a note** — click **Add note** in the browser and fill in the form.

---

## Project structure

```
app.py            Flask routes, form handling, validation, SQLite queries
schema.sql        SQL to create the notes table
requirements.txt  Python packages required to run the app
static/
  style.css       Page styling
  script.js       Client-side JavaScript (delete confirmation, character counter)
  img/            Images served by Flask
templates/
  base.html       Shared page layout
  index.html      Lists all notes
  add.html        Form to add a new note
  edit.html       Form to edit an existing note
docs/             Beginner guides for each technology used
```

---

## Further help

| File | What it covers |
|---|---|
| [docs/html.md](docs/html.md) | Page structure and forms |
| [docs/css.md](docs/css.md) | Styling and layout |
| [docs/javascript.md](docs/javascript.md) | Client-side behaviour |
| [docs/flask.md](docs/flask.md) | Routes and server-side Python |
| [docs/jinja.md](docs/jinja.md) | Templates and dynamic pages |
| [docs/sqlite.md](docs/sqlite.md) | Simple SQL database storage |

