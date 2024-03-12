#!/usr/bin/node

const args = process.argv.slice(2);
let secondMax = 0;

if (args.length > 1) {
  const integers = args.map(Number);
  integers.sort((a, b) => b - a);
  secondMax = integers[1];
}

console.log(secondMax);
