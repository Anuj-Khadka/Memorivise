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
let searchIcon = document.getElementById("search-icon");
let searchExpand = document.getElementById("search-expand");
let searchSubmit = document.getElementById("search-submit");

searchIcon.addEventListener("click", () => {
  searchIcon.classList.add("d-none");
  searchExpand.classList.remove("d-none");
});

searchSubmit.addEventListener("click", () => {
  searchIcon.classList.toggle("d-none");
  searchExpand.classList.toggle("d-none");
});

//revise_modal

// let reviseTest = document.getElementById("revise_test");

// reviseTest.addEventListener("click",  (e) => {
//   let docBody = document.getElementsByTagName("body");
//   docBody.innerHTML += `
//   <div class="modal fade" id="testModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
//               <div class="modal-dialog modal-dialog-centered" role="document">
//                 <div class="modal-content">
//                   <div class="modal-header">
//                     <h5 class="modal-title" id="exampleModalCenterTitle">Example Modal</h5>
//                     <button type="button" class="close" data-dismiss="modal" aria-label="Close">
//                       <span aria-hidden="true">&times;</span>
//                     </button>
//                   </div>
//                   <div class="modal-body">
//                     <form>
//                       <div class="form-group">
//                         <label for="exampleFormControlInput1">Email address</label>
//                         <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
//                       </div>
//                       <div class="form-group">
//                         <label for="exampleFormControlSelect1">Example select</label>
//                         <select class="form-control" id="exampleFormControlSelect1">
//                           <option>1</option>
//                           <option>2</option>
//                           <option>3</option>
//                           <option>4</option>
//                           <option>5</option>
//                         </select>
//                       </div>
//                       <div class="form-group">
//                         <label for="exampleFormControlTextarea1">Example textarea</label>
//                         <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
//                       </div>
//                     </form>
//                   </div>
//                   <div class="modal-footer">
//                     <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
//                     <button type="button" class="btn btn-primary">Save changes</button>
//                   </div>
//                 </div>
//               </div>
//             </div>
//   `;
// });
