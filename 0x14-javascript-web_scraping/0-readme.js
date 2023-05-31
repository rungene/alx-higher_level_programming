#!/usr/bin/node

const fileSys = require('fs');

const filePath = process.argv[2];

fileSys.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
