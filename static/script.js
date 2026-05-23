document.querySelectorAll(".delete-form").forEach((form) => {
    form.addEventListener("submit", (event) => {
        if (!window.confirm("Delete this note?")) {
            event.preventDefault();
        }
    });
});
