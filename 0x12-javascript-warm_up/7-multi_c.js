#!/usr/bin/node
/* Prints x times "C is fun" where x is the first argv */

if (!process.argv[2] || isNaN(parseInt(process.argv[2], 10))) {
  console.log('Missing number of ocurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
