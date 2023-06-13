#!/usr/bin/node

str1 = 'is';
str2 = 'undefined';

if (!process.argv[2]) {
  console.log('undefined is undefined');
} else if (process.argv.length === 3) {
  let result = process.argv[2].concat(" ", str1, " ",  str2);
  console.log(result);
} else if (process.argv.length >= 3){
  let result = process.argv[2] + ' ' + str1 + ' ' + process.argv[3];
  console.log(result);
}
