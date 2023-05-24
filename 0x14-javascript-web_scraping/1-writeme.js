#!/usr/bin/node

const fileSys = require('fs');

const filePath = process.argv[2];
const strContent = process.argv[3];

fileSys.writeFile(filePath, strContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
