#!/usr/bin/node
// getting command line args
const args = process.argv.slice(2);

// check if args were paassed
if (args[0]) {
  console.log(`${args}`);
} else {
  console.log('No argument');
}
