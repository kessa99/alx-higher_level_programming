#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument');
}
for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] !== 2) {
    console.log(process.argv[i]);
  }
}
