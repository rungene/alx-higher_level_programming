#!/usr/bin/node
// getting command line args
const args = process.argv.slice(2);

// check if args were paassed
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Argument found');
}
