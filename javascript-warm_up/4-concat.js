#!/usr/bin/node

const a = process.argv[2] ? process.argv[2] : 'undefined';
const b = process.argv[3] ? process.argv[3] : 'undefined';

console.log(`${a} is ${b}`);