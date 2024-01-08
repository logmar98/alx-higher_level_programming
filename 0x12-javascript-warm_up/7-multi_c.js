#!/usr/bin/node
let  x = process.argv[2];
let num = Math.floor(Number(x));
if (!isNaN(num)) {
    for (let i = 0; i < x; i++) {
        console.log("C is fun");
    }
} else {
    console.log("Missing number of occurrences");
}
