#!/usr/bin/node

let arg = process.argv[2];
arg = parseInt(arg);

function recursion (n) {
  if (!n || n <= 1) return 1;

  return n * recursion(n - 1);
}

console.log(`${recursion(arg)}`);