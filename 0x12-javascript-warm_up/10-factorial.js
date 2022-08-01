#!/usr/bin/node
const process = require('process');
const arg = process.argv[2];
function factorial (arg) {
  if (isNaN(arg) || arg === 0) {
    return 1;
  }
  return arg * factorial(arg - 1);
}
console.log(factorial(parseInt(arg)));
