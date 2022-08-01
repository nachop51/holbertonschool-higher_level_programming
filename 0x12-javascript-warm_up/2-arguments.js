#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
