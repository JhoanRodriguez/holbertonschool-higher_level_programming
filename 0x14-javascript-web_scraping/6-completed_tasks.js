#!/usr/bin/node
/* Script that computes the number of tasks completed by user id */
const req = require('request');
let result = '';
const object = {};

req(process.argv[2], function (error, stat, data) {
  if (error) {
    console.log(error);
  } else {
    result = JSON.parse(data);
    for (let i = 0; i < result.length; i++) {
      if (result[i].completed === true) {
        if (isNaN(object[result[i].userId])) {
          object[result[i].userId] = 0;
        }
        object[result[i].userId] += 1;
      }
    }
  }
  console.log(object);
});
