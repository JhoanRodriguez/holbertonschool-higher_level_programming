#!/usr/bin/node
/* Writes a string to a file */
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
