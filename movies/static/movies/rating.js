document.addEventListener("DOMContentLoaded", () => {
  const stars = document.querySelectorAll(".star");
  const input = document.getElementById("rating-value");
  const form = document.getElementById("rating-form");
  const container = document.getElementById("star-rating");

  let currentRating = parseFloat(container.dataset.userRating) || 0;

  // подсветить при загрузке
  highlight(currentRating);

  stars.forEach((star, index) => {
    star.addEventListener("mousemove", (e) => {
      const rect = star.getBoundingClientRect();
      const isHalf = e.clientX - rect.left < rect.width / 2;
      const value = index + (isHalf ? 0.5 : 1);
      highlight(value);
    });

    star.addEventListener("mouseleave", () => {
      highlight(currentRating);
    });

    star.addEventListener("click", (e) => {
      const rect = star.getBoundingClientRect();
      const isHalf = e.clientX - rect.left < rect.width / 2;
      currentRating = index + (isHalf ? 0.5 : 1);
      input.value = currentRating;
      form.submit();
    });
  });

  function highlight(rating) {
    stars.forEach((star, i) => {
      star.classList.remove("active", "half");

      if (i + 1 <= rating) {
        star.classList.add("active");
      } else if (i + 0.5 === rating) {
        star.classList.add("half");
      }
    });
  }
});
