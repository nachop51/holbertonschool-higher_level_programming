#!/usr/bin/node
const process = require('process');
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return parseInt(a) + parseInt(b);
}
console.log(add(a, b));
