#!/usr/bin/node

function recursion (n) {
  if (!n || n <= 1) return 1;

  return n * recursion(n - 1);
}

let arg = process.argv[2];
arg = parseInt(arg);

console.log(`${recursion(arg)}`);
