#!/usr/bin/node
const Rectangle = require('./5-square');

module.exports =
  class Square extends Rectangle {
    charPrint (c = 'X') {
      const charPrint = c === undefined ? 'X' : c;
      for (let row = 0; row < this.height; row++) {
        for (let col = 0; col < this.width; col++) {
          process.stdout.write(charPrint);
        }
        console.log('');
      }
    }
  };
