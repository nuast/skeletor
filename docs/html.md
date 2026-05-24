# HTML

## What is HTML?

HTML (HyperText Markup Language) is the language used to describe the structure and content of a web page. It tells the browser what is on the page — headings, paragraphs, forms, links, and images — but not how they should look.

## What does HTML do in this app?

Every page the user sees is built from an HTML template. When the browser requests a page, Flask fills in the data and sends back an HTML document. The browser then reads that HTML and displays it.

## Where is it in the project?

All HTML lives in the `templates/` folder:

| File | What it renders |
|---|---|
| `templates/base.html` | Shared layout used by every page |
| `templates/index.html` | The list of all notes |
| `templates/add.html` | The form for adding a new note |
| `templates/edit.html` | The form for editing an existing note |

## Important ideas

### Tags and elements

HTML uses opening and closing tags to mark up content:

```html
<h1>Revision Notes</h1>
<p>A tiny Flask CRUD app.</p>
```

### Nesting

Elements are placed inside one another to build structure:

```html
<article class="card">
    <h2>Photosynthesis</h2>
    <p class="note-meta">Topic: Biology</p>
</article>
```

### Forms

Forms let users send data to the server. The `method="post"` attribute tells the browser to send the data in the request body rather than in the URL.

```html
<form action="/add" method="post">
    <input name="title" type="text">
    <button type="submit">Save</button>
</form>
```

In this app, every form that changes data — add, edit, and delete — uses `method="post"`. Flask reads the submitted values with `request.form`.

### The `id` and `class` attributes

- `id` identifies a **single** element (e.g. `id="content"`).
- `class` labels elements that share the same style or behaviour (e.g. `class="card"`).

CSS uses these attributes to apply styles. JavaScript uses them to find elements.

## Try changing this

Open `templates/base.html` and change the `<h1>` text:

```html
<h1>My Revision App</h1>
```

Refresh the browser. The heading should update on every page because all templates share the same base layout.
