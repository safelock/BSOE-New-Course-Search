// Global variables
var courseInput = document.querySelector('#course');
var newCourse = document.querySelector('#new-course');
var description = document.querySelector('#desc');
const myForm = document.querySelector('#my-form');
const msg = document.querySelector('.msg');


// Convert old course to the new one with description
function onSubmit(e) {
  e.preventDefault();
  var upperNew = `${courseInput.value}`.toString().toUpperCase();
  var convert = convCourse[upperNew][0];
  var desc = convCourse[upperNew][1];
  newCourse.textContent = convert;
  description.textContent = desc;
}

// Where the magic begins
function main(){
  myForm.addEventListener('submit', onSubmit);
}

// Calls main()
main();
const convCourse = {};
