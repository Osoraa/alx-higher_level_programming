#!/usr/bin/node

let i = parseInt(process.argv[2]);
if (!i) {
  console.log('Missing number of occurrences');
}

while (i--) {
  console.log('C is fun');
}
