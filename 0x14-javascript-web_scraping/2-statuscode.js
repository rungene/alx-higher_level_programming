#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
    return;
  }
  console.log('code:', response.statusCode); // Print the response status code if a response was received
});
