#!/usr/bin/node

function add (a, b) {
  const res = a + b;
  return res;
}

// getting third command line args
const arg = parseInt(process.argv[2]);
const arg1 = parseInt(process.argv[3]);

// additions and loging
const addition = add(arg, arg1);
console.log(addition);
