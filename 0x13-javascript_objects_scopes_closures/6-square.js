#!/usr/bin/node

const sqr = require('./5-square');

class Square extends sqr {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    this.print(c);
  }
}
module.exports = Square;
