#!/usr/bin/node

const arg = process.argv[2];
const num = isNaN(arg);

if (num) {
  console.log('NaN');
} else {
  const arg1 = parseInt(process.argv[2]);
  const arg2 = parseInt(process.argv[3]);
  const result = arg1 + arg2;
  console.log(result);
}
