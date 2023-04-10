#!/usr/bin/node

const a = process.argv[2];
const num = parseInt(a);

console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);