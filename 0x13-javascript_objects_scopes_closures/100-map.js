#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map(function (item) {
  if (this.index === undefined) this.index = -1;
  this.index++;
  return item * this.index;
});
console.log(list);
console.log(newList);
