import initLibheif from "https://unpkg.com/libheif-js/libheif-wasm/libheif-bundle.mjs";

function main() {
  window.addEventListener("load", decode_all_heif);
}
main();

async function decode_heif(elem) {
  async function inner(elem) {
    let imageUrl = elem.src;

    let response = await fetch(imageUrl);
    if (!response.ok) {
      throw new Error(`Failed to fetch ${imageUrl}`);
    }

    let file = await response.arrayBuffer();

    let libheif = await initLibheif();
    let decoder = new libheif.HeifDecoder();
    let data = decoder.decode(file);

    if (!data || data.length === 0) {
      throw new Error("No image data decoded from HEIF file.");
    }

    let heifImage = data[0];
    let width = heifImage.get_width();
    let height = heifImage.get_height();

    let canvas = document.createElement("canvas");
    canvas.width = width;
    canvas.height = height;

    let ctx = canvas.getContext("2d");
    let imageData = ctx.createImageData(width, height);

    await new Promise((resolve, reject) => {
      heifImage.display(imageData, (displayData) => {
        if (!displayData) {
          return reject(new Error("HEIF processing error"));
        }
        resolve();
      });
    });

    ctx.putImageData(imageData, 0, 0);

    canvas.addEventListener("click", function () {
      open_canvas(canvas);
    });
    canvas.style.cursor = "pointer";

    return canvas;
  }

  try {
    let canvas = await inner(elem);
    return canvas;
  } catch (error) {
    console.error("Error decoding HEIC image:", error);
  }
}

async function decode_all_heif() {
  let images = document.querySelectorAll("img");
  for (let elem of images) {
    let imageUrl = elem.src;

    if (
      !imageUrl.toLowerCase().endsWith(".heic") &&
      !imageUrl.toLowerCase().endsWith(".heif")
    ) {
      continue;
    }

    let canvas = await decode_heif(elem);

    let div = document.createElement("div");
    div.classList.add("photo-box2");
    div.innerHTML = `
<div class="bg">
  <div class="bg2"></div>
</div>
`;
    div.querySelector(".bg2").appendChild(canvas);
    elem.replaceWith(div);
  }
}

function open_canvas(canvas) {
  canvas.toBlob((blob) => window.open(URL.createObjectURL(blob), "_blank"));
}
