// querySelectorAll returns every element matching a CSS selector as a list.
const deleteForms = document.querySelectorAll(".delete-form");

for (const form of deleteForms) {
    form.addEventListener("submit", function (event) {
        // JavaScript runs in the browser, so it can react before the form is sent.
        // preventDefault() stops the browser submitting the form to Flask.
        if (!window.confirm("Delete this note?")) {
            event.preventDefault();
        }

        // Flask must still check requests on the server.
        // Browser-side JavaScript improves usability, but it is not validation.
    });
}

// getElementById returns the single element with that id.
// Here we use it to find the content textarea and show a live character count.
const contentBox = document.getElementById("content");

if (contentBox) {
    const counter = document.createElement("p");
    counter.id = "char-count";
    contentBox.after(counter);

    function updateCount() {
        counter.textContent = contentBox.value.length + " characters";
    }

    contentBox.addEventListener("input", updateCount);
    updateCount();
}
