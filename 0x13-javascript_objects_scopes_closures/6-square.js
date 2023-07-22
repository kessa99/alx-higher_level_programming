#!/usr/bin/node

const Squar = require('./5-square');

module.exports = class Square extends Squar {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        output += c;
      }
      for (let j = 0; j < this.width; j++) {
        console.log(output);
      }
    }
  }
};
