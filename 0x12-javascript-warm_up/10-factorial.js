#!/usr/bin/node
const arg1 = process.argv[2];
const num = Math.floor(Number(arg1));

function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
console.log(factorial(num));
