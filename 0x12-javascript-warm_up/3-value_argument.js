#!/usr/bin/node
/* Prints the first argv passed */

const myArgs = process.argv;

if (!myArgs[2]) {
  console.log('No argument');
} else {
  console.log(myArgs[2]);
}
