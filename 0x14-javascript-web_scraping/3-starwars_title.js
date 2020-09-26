#!/usr/bin/node
/* Script that prints the title of a Star Wars movie
   where the episode number matches a given integer */
const req = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
let content = '';

req(url + process.argv[2], function (err, query, data) {
  if (err) {
    console.log(err);
  } else {
    content = JSON.parse(data);
    console.log(content.title);
  }
});
