#!/usr/bin/node

function fact (n) {
  if (!n || n <= 1) return 1;

  return n * fact(n - 1);
}

let arg = process.argv[2];
arg = parseInt(arg);

console.log(`${fact(arg)}`);
