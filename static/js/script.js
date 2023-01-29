// let descriptionBox = document.getElementById("description");
// let submitBtn = document.getElementById("submit");
// descriptionBox.addEventListener("keypress", (e) => {
//   if (e.key == "Enter") {
//     e.preventDefault();
//     submitBtn.click();
//   }
//   if (e.key == "Enter" && e.shiftKey) {
//     e.preventDefault();
//     console.log("hihihi");
//   }
// });


// search icon in navbar
let searchIcon = document.getElementById("search-icon")
let searchExpand = document.getElementById("search-expand")
let searchSubmit = document.getElementById("search-submit")

searchIcon.addEventListener("click", ()=>{
  searchIcon.classList.add("d-none")
  searchExpand.classList.remove("d-none")
})


searchSubmit.addEventListener("click", ()=>{
  searchIcon.classList.toggle("d-none")
  searchExpand.classList.toggle("d-none")

})