#!/usr/bin/node
/*
 * Write a JavaScript script that toggles the class of the <hea
 * er> element when the user clicks on the tag DIV#toggle_heade
 * :
 * The <header> element must always have one class: red or gree
 * never both in the same time and never empty.
 * If the current class is red, when the user click on DIV#togg
 * e_header, the class must be updated to green ; and the rever
 * e.
 * You can’t use document.querySelector to select the HTML tag
 * You must use the JQuery API
*/

$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green')
  });
});
