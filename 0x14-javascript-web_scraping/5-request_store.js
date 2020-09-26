#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file */

const myFile = require('fs');
const req = require('request');

req(process.argv[2], function (error, stat, data) {
  if (error) {
    console.log(error);
  } else {
    myFile.writeFile(process.argv[3], data, 'utf8', function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
