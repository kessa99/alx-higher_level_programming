#!/usr/bin/node
/*
 * Write a JavaScript script that updates the text of the <head
 * r> element to New Header!!! when the user clicks on DIV#upda
 * e_header
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
*/

$(document).ready(function () {
  $('#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
