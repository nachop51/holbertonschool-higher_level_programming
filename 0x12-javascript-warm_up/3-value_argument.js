#!/usr/bin/node
const process = require('process');
if (process.argv.length === 2) {
  console.log('No argument');
} else {
  process.argv.slice(2).forEach((val) => {
    console.log(`${val}`);
  });
}
