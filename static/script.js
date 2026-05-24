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
