#!/usr/bin/node

const str1 = 'is';
const str2 = 'undefined';

if (!process.argv[2]) {
  console.log('undefined is undefined');
} else if (process.argv.length === 3) {
  const result = process.argv[2].concat(' ', str1, ' ', str2);
  console.log(result);
} else if (process.argv.length >= 3) {
  const result = process.argv[2] + ' ' + str1 + ' ' + process.argv[3];
  console.log(result);
}
