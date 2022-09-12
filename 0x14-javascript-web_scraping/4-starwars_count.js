#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;

axios
  .get(args[2])
  .then((response) => {
    let times = 0;
    for (const i in response.data.results) {
      if (
        response.data.results[i].characters.includes(
          'https://swapi-api.hbtn.io/api/people/18/'
        )
      ) {
        ++times;
      }
    }
    console.log(times);
  })
  .catch((error) => {
    console.log(error);
  });
