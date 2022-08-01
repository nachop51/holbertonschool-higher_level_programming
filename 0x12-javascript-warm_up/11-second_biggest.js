#!/usr/bin/node
const process = require('process');
const array = process.argv.slice(2);
if (array.length === 0 || array.length === 1) {
  console.log(0);
} else if (array.length > 1) {
  let max = parseInt(array[0]);
  let second = -Infinity;
  for (let i = 1; i < array.length; i++) {
    if (max < parseInt(array[i])) {
      max = parseInt(array[i]);
    }
  }
  for (let i = 0; i < array.length; i++) {
    if (second < max && max !== parseInt(array[i]) && parseInt(array[i]) > second) {
      second = array[i];
    }
  }
  console.log(second);
}
