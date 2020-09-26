#!/usr/bin/node
/* Class Square that inherits from class Square */

const SquareOriginal = require('./5-square');
class Square extends SquareOriginal {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
