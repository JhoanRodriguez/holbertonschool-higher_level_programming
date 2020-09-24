#!/usr/bin/node
/* Prints a square */

if (!process.argv[2] || isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
