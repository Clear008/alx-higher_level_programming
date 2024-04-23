#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body).reduce((accumulator, crt) => {
    if (!accumulator[crt.userId]) {
      if (crt.completed) {
        accumulator[crt.userId] = 1;
      }
    } else {
      if (crt.completed) {
        accumulator[crt.userId] += 1;
      }
    }
    return accumulator;
  }, {});
  console.log(dict);
});
