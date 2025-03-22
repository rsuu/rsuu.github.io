document.querySelectorAll(".carousel-card").forEach((card) => {
  f(card);
});

function f(card) {
  let content = card.querySelector(".carousel");
  let scrollbar = card.querySelector(".scrollbar");
  let thumb = card.querySelector(".thumb");
  let scrollTimeout;

  // 滚动监听
  content.addEventListener("scroll", () => {
    showScrollbar();
    updateThumb();

    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(hideScrollbar, 500);
  });

  function updateThumb() {
    let scrollWidth = content.scrollWidth;
    let clientWidth = content.clientWidth;
    let scrollbarWidth = scrollbar.offsetWidth;

    let thumbWidth = Math.max((clientWidth / scrollWidth) * scrollbarWidth, 20);
    let maxScroll = scrollWidth - clientWidth;
    let scrollLeft = content.scrollLeft;
    let thumbPosition =
      (scrollLeft / maxScroll) * (scrollbarWidth - thumbWidth);

    thumb.style.width = `${thumbWidth}px`;
    thumb.style.left = `${thumbPosition}px`;
  }

  function showScrollbar() {
    scrollbar.style.opacity = 1;
  }

  function hideScrollbar() {
    scrollbar.style.opacity = 0;
  }
}
