#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

console.log(isNaN(number) ? 'Not a number' : 'My number: ' + number);
