#!/usr/bin/node
const process = require('process');
const size = process.argv[2];
if (!size || isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
