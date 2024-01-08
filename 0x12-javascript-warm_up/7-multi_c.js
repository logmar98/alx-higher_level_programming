#!/usr/bin/node
const x = process.argv[2];
const num = Math.floor(Number(x));
if (!isNaN(num)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
