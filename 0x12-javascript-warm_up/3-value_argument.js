#!/usr/bin/node
const process = require('process');
if (!process.argv.slice(2)[0]) {
  console.log('No argument');
} else {
  process.argv.slice(2).forEach((val) => {
    console.log(`${val}`);
  });
}
