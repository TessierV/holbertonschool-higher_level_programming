#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, function (error, response, body) {
  if (error) return;

  const movies = JSON.parse(body).results;

  let count = 0;

  for (const movie of movies) {
    for (const char of movie.characters) {
      /* Wedge Antilles = 18 */
      if (char.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
