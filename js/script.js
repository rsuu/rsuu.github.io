function main() {
  theme();
  zodiac();
}
main();

function theme() {
  const setTheme = (theme) => {
    document.documentElement.className = theme;

    localStorage.setItem("theme", theme);
  };

  const hasCodeRun = localStorage.getItem("hasCodeRun");

  if (!hasCodeRun) {
    const defaultTheme = "{{ config.extra.default_theme }}";
    setTheme(defaultTheme);
    localStorage.setItem("hasCodeRun", "true");
  }

  const getTheme = () => {
    const theme = localStorage.getItem("theme");
    if (theme) {
      setTheme(theme);
    }
  };

  getTheme();
}

function zodiac() {
  document.querySelectorAll(".zodiac").forEach((elem) => {
    let year = parseInt(elem.getAttribute("year"));
    let y = ((year - 1900) % 12) + 1;
    elem.innerHTML = `
<img alt="icons" src="/svg/zodiac/${y}.svg" />
`;
  });
}
