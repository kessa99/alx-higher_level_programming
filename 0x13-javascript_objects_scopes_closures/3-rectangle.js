#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof (h) === 'number' && typeof (w) === 'number') {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let output = '';
    for (let i = 0; i < this.width; i++) {
      output += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(output);
    }
  }
};
