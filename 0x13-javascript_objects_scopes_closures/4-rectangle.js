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

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    // width / height properties mupliplied by 2
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
