#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;

axios
  .get(args[2])
  .then((response) => {
    let times = 0;
    for (const i in response.data.results) {
      for (const j in response.data.results[i].characters) {
        if (response.data.results[i].characters[j].includes('18')) {
          ++times;
          break;
        }
      }
    }
    console.log(times);
  })
  .catch((error) => {
    console.log(error);
  });
