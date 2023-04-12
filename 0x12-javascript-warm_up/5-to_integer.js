#!/usr/bin/node
// getting third command line args
const arg = process.argv[2];
const num = parseInt(arg);

// check if arg was int
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
