#!/usr/bin/node
const num = process.argv[2];
const x = Math.floor(Number(num));

if (!isNaN(num)) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
