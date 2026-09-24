(() => {
  const storageKey = "estatelink-theme";
  const root = document.documentElement;

  const toggle = document.querySelector(".theme-toggle-input");

  const setTheme = (theme, savePreference = true) => {
    const isDark = theme === "dark";
    root.dataset.theme = isDark ? "dark" : "light";
    if (toggle) {
      toggle.checked = isDark;
    }
    if (savePreference) {
      try {
        localStorage.setItem(storageKey, root.dataset.theme);
      } catch (error) {
        // The current session can still use the selected theme if storage is unavailable.
      }
    }

    document.querySelectorAll(".theme-toggle").forEach((label) => {
      label.textContent = isDark ? "☼ Light theme" : "☾ Dark theme";
    });
  };

  let savedTheme = "light";
  try {
    savedTheme = localStorage.getItem(storageKey) === "dark" ? "dark" : "light";
  } catch (error) {
    // Use the default light theme when browser storage is unavailable.
  }

  if (toggle) {
    toggle.addEventListener("change", () => setTheme(toggle.checked ? "dark" : "light", true));
  }

  setTheme(savedTheme, false);
})();
