#!/usr/bin/node

const arg = process.argv[2];
const num = isNaN(arg);

if (num) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);
  let output = '';
  for (let i = 0; i < size; i++) {
    output += 'x';
  }
  for (let j = 0; j < size; j++) {
    console.log(output);
  }
}
