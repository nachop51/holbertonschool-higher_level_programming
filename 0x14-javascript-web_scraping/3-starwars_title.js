#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;

axios
  .get('https://swapi-api.hbtn.io/api/films/' + args[2])
  .then((response) => {
    console.log(response.data.title);
  })
  .catch((error) => {
    console.log(error);
  });
