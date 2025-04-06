document.querySelectorAll("pre:not(.mermaid)").forEach((block) => {
  let code_bar = document.createElement("div");
  code_bar.className = "code-bar";

  code_bar.innerHTML = `
    <div class="lang"></div>
    <div class="copy" role="button"></div>
  `;

  block.prepend(code_bar);
});
