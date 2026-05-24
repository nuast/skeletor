# JavaScript

## What is JavaScript?

JavaScript is a programming language that runs **in the browser**. Unlike Python (which runs on the server), JavaScript can react to what a user does on the page without sending a request to Flask first.

## What does JavaScript do in this app?

`static/script.js` does two things:

1. **Delete confirmation** — asks the user "Delete this note?" before the delete form is submitted.
2. **Character counter** — shows a live character count below the content textarea on the add and edit pages.

## Where is it in the project?

```
static/script.js
```

It is linked at the bottom of every page in `base.html`:

```html
<script src="{{ url_for('static', filename='script.js') }}"></script>
```

## Important ideas

### The DOM

The DOM (Document Object Model) is the browser's representation of the HTML on the page. JavaScript can read and change the DOM to react to user actions.

### Selecting elements

```js
// Select all elements with class="delete-form"
const deleteForms = document.querySelectorAll(".delete-form");

// Select the single element with id="content"
const contentBox = document.getElementById("content");
```

### Event listeners

An event listener runs a function when something happens:

```js
form.addEventListener("submit", function (event) {
    if (!window.confirm("Delete this note?")) {
        event.preventDefault();  // stop the form being sent
    }
});
```

`event.preventDefault()` stops the browser's default action — in this case, submitting the form.

### Creating elements

JavaScript can add new elements to the page:

```js
const counter = document.createElement("p");
counter.textContent = "0 characters";
contentBox.after(counter);  // insert after the textarea
```

### Client-side vs server-side

JavaScript improves the user experience but it **cannot replace server-side validation**. A user could disable JavaScript in their browser or send a request directly. Flask always validates the data again on the server.

## Try changing this

Open `static/script.js` and change the confirmation message:

```js
if (!window.confirm("Are you sure you want to delete this note?")) {
```

Refresh the browser, try clicking Delete, and see the new message appear.
