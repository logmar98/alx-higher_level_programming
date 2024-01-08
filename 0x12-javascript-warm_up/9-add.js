#!/usr/bin/node
let a = Number(process.argv[2]);
let b = Number(process.argv[3]);

function add(a, b) {
    let result = a + b;
    console.log(result);
}
add(a, b);
