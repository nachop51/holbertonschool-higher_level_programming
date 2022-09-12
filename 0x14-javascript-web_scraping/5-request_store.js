#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const args = process.argv;

axios
  .get(args[2])
  .then((response) => {
    fs.writeFile(
      args[3],
      JSON.stringify(response.data),
      'utf8',
      function (err) {
        if (err) {
          console.log(err);
        }
      }
    );
  })
  .catch((error) => {
    console.log(error);
  });
