#!/usr/bin/node

const fileSys = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

// make a get request to the url
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fileSys.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
