#!/usr/bin/node
let arg1 = process.argv[2];
let num = Math.floor(Number(arg1));

function factorial(num) {
    if (num === 0) {
        return 1;
    } else {
        return num * factorial(num - 1);
    }
}
console.log(factorial(num));
