#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeAntilles = films.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${wedgeAntilles.length}`);
  }
});
