#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);

if (num) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
