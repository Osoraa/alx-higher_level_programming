#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!size) {
  console.log('Missing size');
}

let result = '';

for (let j = 0; j < size; j++) {
  result += 'X';
}

for (let i = 0; i < size; i++) {
  console.log(result);
}
