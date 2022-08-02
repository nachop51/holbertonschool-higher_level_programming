#!/usr/bin/node
const fs = require('fs');
const process = require('process');
let str = '';
str += fs.readFileSync(process.argv[2]).toString();
str += fs.readFileSync(process.argv[3]).toString();
fs.writeFile(process.argv[4], str, function (err) {
  if (err) {
    return console.error(err);
  }
});
