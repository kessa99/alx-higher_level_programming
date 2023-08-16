#!/usr/bin/node
/*
 * Write a JavaScript script that updates the text color of the
 * <header> element to red (#FF0000) when the user clicks on th
 * tag DIV#red_header:
 * You can’t use document.querySelector to select the HTML ta
 * You must use the JQuery API
*/

$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').css('color', '#FF0000');
  })
});
