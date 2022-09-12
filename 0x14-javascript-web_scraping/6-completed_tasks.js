#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;

axios
  .get(args[2])
  .then((response) => {
    const tasks = response.data;
    const completed = {};
    for (const task in tasks) {
      if (isNaN(completed[tasks[task].userId]) && tasks[task].completed) {
        completed[tasks[task].userId] = 0;
      }
      if (tasks[task].completed) {
        completed[tasks[task].userId] += 1;
      }
    }
    console.log(completed);
  })
  .catch((error) => {
    console.log(error);
  });
