#!/usr/bin/node
const process = require('process');
const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myVar);
}
