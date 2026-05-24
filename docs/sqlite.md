# SQLite

## What is SQLite?

SQLite is a simple file-based database. All the data is stored in a single file (`notes.db`) rather than on a separate database server. It is ideal for small projects and learning because no extra software needs to be installed.

## What does SQLite do in this app?

SQLite stores every note the user creates. When Flask needs to display notes, it queries the database and gets the data back as rows. When a note is added, edited, or deleted, Flask runs the appropriate SQL statement to update the database.

## Where is it in the project?

| File | Purpose |
|---|---|
| `schema.sql` | Contains the SQL to create the `notes` table |
| `notes.db` | The database file — created automatically when the app first runs |
| `app.py` | Contains all the SQL queries the app uses |

## The notes table

The table is defined in `schema.sql`:

```sql
CREATE TABLE notes (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    title   TEXT NOT NULL,
    topic   TEXT NOT NULL,
    content TEXT NOT NULL
);
```

Each row represents one note. `id` is assigned automatically.

## Important ideas

### SELECT — reading data

```sql
SELECT id, title, topic, content FROM notes ORDER BY id DESC
```

Flask uses this to fetch all notes and pass them to the index template.

### INSERT — adding data

```sql
INSERT INTO notes (title, topic, content) VALUES (?, ?, ?)
```

The `?` placeholders are filled in by Python. Using placeholders instead of string formatting protects against SQL injection.

### UPDATE — editing data

```sql
UPDATE notes SET title = ?, topic = ?, content = ? WHERE id = ?
```

Only the row with the matching `id` is changed.

### DELETE — removing data

```sql
DELETE FROM notes WHERE id = ?
```

Only the row with the matching `id` is removed.

### Parameterised queries

Notice that all queries in `app.py` use `?` placeholders rather than putting values directly into the SQL string. This is called a **parameterised query** and it is important for security. It stops a user from entering SQL code into a form field and having it run against your database.

### Initialising and resetting the database

To reset the database (this deletes all notes):

```bash
flask --app app init-db
```

## Try changing this

Open `schema.sql` and add a new column for a priority level:

```sql
priority INTEGER NOT NULL DEFAULT 1
```

Then reset the database with `flask --app app init-db`, restart the app, and check that the table now has the new column by adding a note.

> **Note:** adding a column to the schema means you will also need to update the `INSERT` and `SELECT` queries in `app.py` and the forms in `templates/add.html` and `templates/edit.html` to use it.
