#!/usr/bin/node
/*
 * The name must be displayed in the HTML tag DIV#character 
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
*/

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    Datatype: 'json',
    success: function(data){
      let charName = data.name;
      $('#character').text(charName);
    },
    error: function(error) {
      console.log('Error')
    }
  })
});
