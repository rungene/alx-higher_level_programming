const $ = window.$;
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  dataType: 'json',
  success: function (response) {
    const movies = response.results;
    const $list = $('UL#list_movies');
    $.each(movies, function (index, movie) {
      $list.append('<li>' + movie.title + '</li>');
    });
  },
  error: function () {
    $('UL#list_movies').append('<li>Error when fetching Movie title</li>');
  }
});
