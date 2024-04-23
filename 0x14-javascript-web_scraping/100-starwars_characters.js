#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const chars = JSON.parse(body).characters;
    chars.forEach((charUrl) => {
      request.get(charUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const character = JSON.parse(charBody).name;
          console.log(character);
        }
      });
    });
  }
});
