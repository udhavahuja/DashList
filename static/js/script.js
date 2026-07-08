//Dark mode and light mode toggle
const themeToggle = document.getElementById("theme-toggle");
const themeIcon = document.getElementById("theme-icon");

function setTheme(theme) {
    document.body.setAttribute("data-theme", theme);

    if (theme === "dark") {
        themeIcon.classList.remove("bi-sun-fill");
        themeIcon.classList.add("bi-moon-fill");
    } else {
        themeIcon.classList.remove("bi-moon-fill");
        themeIcon.classList.add("bi-sun-fill");
    }

    localStorage.setItem("theme", theme);
}

const savedTheme = localStorage.getItem("theme") || "light";
setTheme(savedTheme);

themeToggle.addEventListener("click", () => {
    const current = document.body.getAttribute("data-theme");

    if (current === "light") {
        setTheme("dark");
    } else {
        setTheme("light");
    }
});
