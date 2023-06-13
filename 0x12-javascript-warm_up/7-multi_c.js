#!/usr/bin/node

const arg = process.argv[2];
const num = isNaN(arg);

if (!arg) {
  console.log('Missing number of occurences');
} else if (num) {
  console.log('Invalid number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
