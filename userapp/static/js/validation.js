const form = document.querySelector('#my-form');

form.addEventListener('submit', function(event) {
    if (!password2.validity.valid) {
        event.preventDefault();
      }
});


const password1 = document.querySelector('#password1');
const password2 = document.querySelector('#password2');
password2.addEventListener('input', function() {
    if (password1.value === password2.value) {
        password2.setCustomValidity('');
    } else {
        password2.setCustomValidity('Passwords do not match');
    }
    // your validation code goes here
});