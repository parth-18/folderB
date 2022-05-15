
var acc = document.getElementsByClassName("accordion");
var i, j;
var panels = document.getElementsByClassName("panel");

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    var sy = this.firstElementChild;
    if (panel.style.maxHeight) {
      panel.style.maxHeight = null;
      $(".faq span").show();
    } else {
      for (j = 0; j < panels.length; j++) {
        panels[j].style.maxHeight = null;
        $(".faq span").show();
      }
      sy.style.display = "none";
      panel.style.maxHeight = panel.scrollHeight + "px";
    }
  });
}
