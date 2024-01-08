#!/usr/bin/node
const arg1 = process.argv[2];
const num = Math.floor(Number(arg1));
if (!isNaN(num)) {
  console.log('My number: ' + String(num));
} else {
  console.log('Not a number');
}
