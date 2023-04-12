#!/usr/bin/node

function add(a, b) {
  let res = a + b;
  return res;
}
// getting third command line args
const arg = process.argv[2];
const arg2 = process.argv[3];

// check if arg was int
if (!arg || !arg2) {
  console.log('NaN');
  process.exit(0)
}
add(arg, arg2);
