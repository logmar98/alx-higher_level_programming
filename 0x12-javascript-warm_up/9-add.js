#!/usr/bin/node
const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

function add (a, b) {
  const result = a + b;
  console.log(result);
}
add(a, b);
