#!/usr/bin/node

const sqr = require('./5-square');

class Square extends sqr {
  // defaults to the character 'X' if it is not provided.
  charPrint (c = 'X') {
    let row = '';

    for (let i = 0; i < this.width; i++) {
      row += c;
    }

    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}
module.exports = Square;
