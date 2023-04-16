#!/usr/bin/node
// getting command line args
const args = process.argv.slice(2);

// check if args were paassed
if (args[0] && args[1]) {
  console.log(`${args[0]} is ${args[1]}`);
} else if (args[0] && !args[1]) {
  console.log(`${args[0]} is undefined`);
} else {
  console.log('undefined is undefined');
}
