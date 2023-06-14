#!/usr/bin/node

if (process.argv.length >= 2) {
  console.log(0);
} else {
  let max = 0;
  for (let i = 2; i < process.argv.length; i++) {
    let num = parseInt(process.argv[i]);

    if (max > num) {
      grd = max;
    } else {
     grd = num;
    }
  }
  console.log(secondMax);
}
