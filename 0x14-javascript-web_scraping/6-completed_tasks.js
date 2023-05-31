#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
// Make a GET request to the url
request.get(url, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
    return;
  }
  // parse json
  const data = JSON.parse(body);

  // store in an object userId and completed tasks count
  const userCompleted = {};

  //  loop through the JSON data and access the properties of each object within the array.
  data.forEach(function (obj) {
    const userId = obj.userId;
    const completed = obj.completed;
    // checks if the task is completed (completed property is true).
    if (completed) {
      // Check if userId exists in userCompleted object. if not, initialize it to 1
      // Otherwise, increment existing count by 1
      userCompleted[userId] = userCompleted[userId] ? userCompleted[userId] + 1 : 1;
    }
  });

  console.log(userCompleted);
});
