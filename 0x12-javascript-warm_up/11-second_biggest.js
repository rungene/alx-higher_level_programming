#!/usr/bin/node

// get the args passed (comand - line)
const args = process.argv.slice(2);

// if no args passed or only one passed, print 0
if (args.length < 2) {
  console.log(0);
  process.exit(0);
}

// biggest and second biggest
let biggest = -Infinity;
let secondBiggest = -Infinity;

// loop through the args as you update the biggest/second biggest
for (let i = 0; i < args.length; i++) {
  const num = parseInt(args[i]);

  if (!isNaN(num)) {
    if (num > biggest) {
      secondBiggest = biggest;
      biggest = num;
    } else if (num > secondBiggest && num !== biggest) {
      secondBiggest = num;
    }
  }
}

// incase no valid ints found in args passed print 0 and exit
if (secondBiggest === -Infinity) {
  console.log(0);
  process.exit(0);
}

console.log(secondBiggest);
