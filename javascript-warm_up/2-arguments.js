#!/usr/bin/node

const argLen = process.argv.splice(2).length;
const result = argLen === 0 ? 'No argument' : 'Argument found';

console.log(result);
