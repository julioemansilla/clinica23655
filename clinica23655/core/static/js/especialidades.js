document.addEventListener("DOMContentLoaded", function() {
    const toggles = document.querySelectorAll(".toggle");

    toggles.forEach(toggle => {
        toggle.addEventListener("click", function() {
            const ul = this.nextElementSibling;
            ul.style.display = ul.style.display === "block" ? "none" : "block";
            this.classList.toggle("active");
        });
    });
});
