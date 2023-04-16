#!/usr/bin/node

// getting command line args(3rd) and parsing to int
const n = parseInt(process.argv[2]);

function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

if (n) {
  const res = factorial(n);
  console.log(res);
} else {
  console.log(1);
}
