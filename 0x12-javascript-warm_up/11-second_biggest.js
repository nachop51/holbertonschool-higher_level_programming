#!/usr/bin/node
const process = require("process");
const array = process.argv.slice(2);
if (array.length === 0 || array.length === 1) {
  console.log(0);
} else if (array.length > 1) {
  var max = Math.max.apply(null, array);
  array.splice(array.indexOf(max), 1);
  console.log(Math.max.apply(null, array));
}
