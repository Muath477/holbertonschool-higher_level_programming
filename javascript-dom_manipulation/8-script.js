// the script is loaded from <head>, so wait until #hello exists in the page
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      document.querySelector('#hello').textContent = data.hello;
    });
});
