#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return (Rectangle + {});
    }
    this.width = w;
    this.height = h;
  }

  print () {
    // rows of rectangle
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      // colums of rectangles
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}
module.exports = Rectangle;
