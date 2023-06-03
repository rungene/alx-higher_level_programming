const $ = window.$;
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json',
  success: function (response) {
    $('DIV#character').text(response.name);
  },
  error: function () {
    $('DIV#character').text('Error fetching character name');
  }
});
