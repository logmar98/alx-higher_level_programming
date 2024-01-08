#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg2) {
  console.log(String('Arguments found'));
} else if (arg1) {
  console.log(String('Argument found'));
} else {
  console.log(String('No argument'));
}
