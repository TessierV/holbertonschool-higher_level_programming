#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const counts = {};

  data.forEach((task) => {
    if (task.completed) {
      const id = task.userId;

      if (!(id in counts)) {
        counts[id] = 0;
      }
      counts[id]++;
    }
  });
  console.log(counts);
});
