#!/usr/bin/node
const process = require('process');
const times = process.argv[2];
if (times && isNaN(times)) {
  console.log('Missing number of occurrences');
} else if (times > 0) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
