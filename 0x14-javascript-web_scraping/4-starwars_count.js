#!/usr/bin/node
const req = require('request');
let counter = 0;
let body = '';

req(process.argv[2], function (error, stat, data) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(data);
    const results = body.results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].match('/18/')) { counter += 1; }
      }
    }
    console.log(counter);
  }
});
