#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);
const sorted = numbers.sort((a, b) => b - a);
console.log(sorted[1] || 0);
