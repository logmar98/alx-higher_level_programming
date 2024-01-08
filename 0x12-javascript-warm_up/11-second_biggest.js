#!/usr/bin/node
let arr = process.argv.slice(2);
let sortedArr = arr.sort((a, b) => b - a);
if (arr.length == 0) {
    console.log(0);
} else if (arr.length == 1) {
    console.log(0);
} else {
    console.log(sortedArr[1]);
}
