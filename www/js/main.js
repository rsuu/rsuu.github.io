async function main() {
  await hl_code();
  dyn_first_letter();
}
main();

async function hl_code() {
  const Parser = window.TreeSitter;
  await Parser.init();
  console.debug("init: tree-sitter");

  let div = document.querySelectorAll("pre code");

  div.forEach(async (elem) => {
    let code_lang = elem.getAttribute("lang");
    let code_text = elem.textContent;

    let path = `/wasm/tree-sitter-${code_lang}.wasm`;
    let parser = new Parser();
    let lang = await Parser.Language.load(path);

    parser.setLanguage(lang);

    let tree = parser.parse(code_text);
    let tree_str = tree.rootNode.toString();

    elem.innerHTML = tree_str;
  });
}

function copyCode() {
  let codeBlock = document.querySelectorAll("code");
  let selection = window.getSelection();
  let range = document.createRange();
  range.selectNodeContents(codeBlock);
  selection.removeAllRanges();
  selection.addRange(range);
  document.execCommand("copy");
  selection.removeAllRanges();
  // You can also give a feedback after copying, like an alert or changing the button text
}

function dyn_first_letter() {
  let n = document.querySelectorAll(".first-letter");
  n.forEach((e) => {
    //document.documentElement.style.setProperty("--letter-size", "3");
    //        e.setAttribute("--letter-size", 1.74rem * 2);
    //            // Get the root element (html)
    //const root = document.documentElement;
    //
    //// Get the computed value of 1rem for the root element
    //const remValue = parseFloat(getComputedStyle(root).fontSize);
    //
    //console.log(remValue); // This will log the value of 1rem in pixels
  });
}

function toggle(elem) {
  let e = elem.querySelector(".popup");

  if (e.style.display == "none") {
    e.style.display = "block";

    window.setTimeout(function () {
      e.style.opacity = 1;
      e.style.transform = "scale(1)";
    }, 0);
  } else {
    e.style.opacity = 0;
    e.style.transform = "scale(0)";
    window.setTimeout(function () {
      e.style.display = "none";
    }, 700);
  }
}
