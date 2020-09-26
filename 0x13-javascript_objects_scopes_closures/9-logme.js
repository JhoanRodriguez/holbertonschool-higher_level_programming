#!/usr/bin/node
/* Function that prints the number of arguments already printed and the new argument value */
let counter = 0;
exports.logMe = function (item) {
  console.log(counter + ':', item);
  counter++;
};
