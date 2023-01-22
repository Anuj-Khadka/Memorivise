let descriptionBox = document.getElementById("description");
let submitBtn = document.getElementById("submit");
descriptionBox.addEventListener("keypress", (e) => {
  if (e.key == "Enter") {
    e.preventDefault();
    submitBtn.click();
  }
  if (e.key == "Enter" && e.shiftKey) {
    e.preventDefault();
    console.log("hihihi");
  }
});
