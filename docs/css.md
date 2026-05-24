# CSS

## What is CSS?

CSS (Cascading Style Sheets) is the language used to control how a web page looks. It describes colours, fonts, spacing, layout, and more. HTML describes *what* is on the page; CSS describes *how it looks*.

## What does CSS do in this app?

The single stylesheet `static/style.css` controls the appearance of every page. Because the stylesheet is linked in `base.html`, it applies everywhere automatically.

## Where is it in the project?

```
static/style.css
```

Flask serves the file directly to the browser. In `base.html` it is linked with:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

## Important ideas

### Selectors

A selector chooses which elements a rule applies to.

| Selector type | Example | What it targets |
|---|---|---|
| Element | `body` | Every `<body>` tag |
| Class | `.card` | Every element with `class="card"` |
| ID | `#content` | The single element with `id="content"` |
| Grouped | `h1, h2, p` | All three element types |

### Properties and values

Each CSS rule pairs a property with a value:

```css
body {
    background-color: #f5f7fb;
    font-family: Arial, sans-serif;
}
```

### The box model

Every HTML element is treated as a box. You can control:

- `padding` — space inside the border
- `margin` — space outside the border
- `border` — the line around the element
- `width` / `height` — the size of the box

### Reusable classes

The `.button` class in `style.css` is applied to both `<a>` links and `<button>` elements across multiple templates. One CSS rule styles them all consistently.

```css
.button,
button {
    background-color: #2563eb;
    color: #ffffff;
    padding: 10px 16px;
}
```

## Try changing this

Open `static/style.css` and change the button colour:

```css
.button,
button {
    background-color: #16a34a;  /* green */
    border-color: #16a34a;
}
```

Refresh the browser. All buttons on every page should change colour.
