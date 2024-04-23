#!/usr/bin/node
const request = require('request');
const api_Url = process.argv[2];

request(api_Url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeAntilles = films.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${wedgeAntilles.length}`);
  }
});

