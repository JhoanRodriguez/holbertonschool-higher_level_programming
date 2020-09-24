#!/usr/bin/node
/* Prints a factorial */

function factorial (a) {
  const num = parseInt(a);
  if (isNaN(num)) {
    return 1;
  }

  if (a === 0) {
    return 1;
  }

  return a * factorial(num - 1);
}

console.log(factorial(process.argv[2]));
