const header = document.querySelector('header');

document.querySelector('#toggle_header').addEventListener('click', function () {
  // setting className replaces every class, so the header never ends up with both
  if (header.classList.contains('red')) {
    header.className = 'green';
  } else {
    header.className = 'red';
  }
});
