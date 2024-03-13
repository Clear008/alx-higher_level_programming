#!/usr/bin/node

const dict = require('./101-data').dict;
const di = {};

for (const ke in dict) {
  if (di[dict[ke]] === undefined) {
    di[dict[ke]] = [ke];
  } else {
    di[dict[ke]].push(ke);
  }
}

console.log(di);
