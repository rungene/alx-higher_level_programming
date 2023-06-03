function fetchMovieTitles() {
  // Make a GET request to the SWAPI API
  var request = new XMLHttpRequest();
  request.open("GET", "https://swapi-api.alx-tools.com/api/films/?format=json");
  request.onload = function() {
    // Check if the request was successful
    if (request.status === 200) {
      // Parse the JSON response
      var response = JSON.parse(request.responseText);
      // Get the movie titles
      var titles = response.results.map(function(movie) {
        return movie.title;
      });
      // Use the JQuery API to select the HTML tag UL#list_movies
      var element = $("#list_movies");
      // Loop through the movie titles and add them as list items
      titles.forEach(function(title) {
        var listItem = $("<li>");
        listItem.text(title);
        element.append(listItem);
      });
    }
  };
  // Send the request
  request.send();
}

// Call the fetchMovieTitles function
fetchMovieTitles();
