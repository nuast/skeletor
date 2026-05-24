# Jinja

## What is Jinja?

Jinja is a **template engine** for Python. It lets you write HTML files that contain placeholders and logic. Flask fills in the placeholders with real data before sending the page to the browser.

## What does Jinja do in this app?

Jinja turns Python data into HTML pages. For example, the `index` route passes a list of notes to `index.html`. Jinja loops through the list and generates a card for each one.

## Where is it in the project?

All templates are in the `templates/` folder. Jinja syntax appears inside `{{ }}` and `{% %}` blocks within the `.html` files.

## Important ideas

### Template inheritance

`base.html` defines the outer structure shared by every page — the `<head>`, header, and `<body>` tags. Other templates *extend* it and fill in the content block.

In `base.html`:

```html
{% block content %}{% endblock %}
```

In `index.html`:

```html
{% extends "base.html" %}

{% block content %}
    <!-- page-specific HTML here -->
{% endblock %}
```

This means you only have to update the layout in one place.

### Outputting variables

Double curly braces print a value into the HTML:

```html
<h2>{{ note.title }}</h2>
<p class="note-meta">Topic: {{ note.topic }}</p>
```

Flask passes `note` to the template with `render_template("index.html", note=note)`.

### Loops

Jinja can loop through a list:

```html
{% for note in notes %}
    <article class="card">
        <h2>{{ note.title }}</h2>
    </article>
{% endfor %}
```

### Conditionals

Jinja can show different HTML depending on a condition:

```html
{% if notes %}
    <!-- show the list -->
{% else %}
    <p>No notes yet.</p>
{% endif %}
```

### `url_for`

`url_for` generates URLs from route names. This means links stay correct even if you change the URL of a route.

```html
<a href="{{ url_for('edit', note_id=note.id) }}">Edit</a>
```

## Try changing this

Open `templates/index.html` and add the note content to the empty state message:

```html
<p>Add your first note using the <strong>Add note</strong> button above.</p>
```

Refresh the browser with no notes in the database to see the change.
