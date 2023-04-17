#!/usr/bin/node
const Request = require('request');
const url = process.argv[2];

Request(url, (error, response, body) => {
	let data = JSON.parse(body);
	let counts = {};
	data.forEach(task => {
		if (task.completed) {
			let id = task.userId;
			if (!counts[id])
				counts[id] = 1;
			else
				counts[id]++;
		}
	});
	console.log(counts);
});