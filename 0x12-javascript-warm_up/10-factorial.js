#!/usr/bin/node

function fact (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

const arg = parseInt(process.argv[2]);
const num = isNaN(arg);
if (num) {
  console.log('NaN');
} else {
  const result = fact(arg);
  console.log(result);
}
