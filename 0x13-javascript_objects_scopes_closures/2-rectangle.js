#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && typeof (h) === 'number' && typeof (w) === 'number') {
      this.w = w;
      this.h = h;
    }
  }
};
