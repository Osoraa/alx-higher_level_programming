#!/usr/bin/node

function filterSort (args) {
  const nums = [];
  for (const arg of args) {
    if (parseInt(arg)) {
      nums.push(parseInt(arg));
    }
  }

  if (nums.length <= 1) {
    return [0, 0];
  } else {
    return nums.sort((a, b) => { return a - b; });
  }
}

const result = filterSort(process.argv.slice(2));

console.log(result[result.length - 2]);
