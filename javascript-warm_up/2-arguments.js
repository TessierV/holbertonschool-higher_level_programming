#!/usr/bin/node

const argLen = process.argv.splice(2).length;
const result = argLen === 0 ? 'No argument' : argLen === 1 ? 'Argument found' : 'Arguments found';

console.log(result);
