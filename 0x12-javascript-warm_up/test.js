#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let max = parseInt(process.argv[2]);
  let secondMax = parseInt(process.argv[2]);

  for (let i = 3; i < process.argv.length; i++) {
    let num = parseInt(process.argv[i]);

    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }

  console.log(secondMax !== max ? secondMax : 0);
}

