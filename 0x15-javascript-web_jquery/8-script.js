#!/usr/bin/node
/*
 * All movie titles must be list in the HTML tag UL#list_movies
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
*/
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    DataType: 'json',
    success: function (data) {
      let movies = data.results;
      let list = $('ul#list_movies')
      movies.forEach(function(movie) {
      list.append('<li>' + movie.title + '</li>');
    });
    },
    error: function() {
      console.log("Error")
    }
  });
});
