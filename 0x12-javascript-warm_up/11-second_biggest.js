#!/usr/bin/node

if (process.argv.length > 2) {
  let grd = process.argv[2];
  let second = 0;

  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > grd) {
      second = grd;
      grd = process.argv[i];
    }
  }
  console.log(second);
} else {
  console.log(0);
}
