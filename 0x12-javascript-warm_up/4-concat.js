#!/usr/bin/node
/* Prints two arguments passed to it, in the following format: “ is ” */

const myArg1 = process.argv[2];
const myArg2 = process.argv[3];

console.log(myArg1 + ' is ' + myArg2);
