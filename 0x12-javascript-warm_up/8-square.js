#!/usr/bin/node

// get command-line args with an exception of the first 2
const args = process.argv.slice(2);

// check if arg is a valid number
const num = parseInt(args[0]);
if (isNaN(num)) {
  console.log('Missing size');
  process.exit(0);
}
for (let i = 0; i < num; i++) {
  console.log('X'.repeat(num));
}
