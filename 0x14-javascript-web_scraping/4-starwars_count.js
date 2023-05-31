#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
// Make a GET request to the url
request.get(url, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
    return;
  }
  // parse json
  const data = JSON.parse(body);
  data.results.forEach(function (result) {
    result.characters.forEach(function (character) {
      const splitChars = character.split('/');
      if (splitChars[splitChars.length - 2] === '18') {
        count++;
      }
    });
  });
  console.log(count);
});
