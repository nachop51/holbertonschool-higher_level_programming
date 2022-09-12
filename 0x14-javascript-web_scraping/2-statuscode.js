#!/usr/bin/node
const axios = require('axios').default;
const args = process.argv;

axios
  .get(args[2])
  .then((response) => {
    console.log('code:', response.status);
  })
  .catch((error) => {
    console.log('code:', error.response.status);
  });
