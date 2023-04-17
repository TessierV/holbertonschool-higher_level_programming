#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get({ url: process.argv[2] }, (error, response, body) => {
  fs.writeFile(process.argv[3], body, (error) => {});
});