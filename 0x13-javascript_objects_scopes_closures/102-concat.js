#!/usr/bin/node

const fs = require('fs');

const fa = fs.readFileSync(process.argv[2], 'utf8');
const fb = fs.readFileSync(process.argv[3], 'utf8');

fs.writeFileSync(process.argv[4], fa + fb);
