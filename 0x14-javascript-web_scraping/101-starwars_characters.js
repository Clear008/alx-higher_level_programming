#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const promises = characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const character = JSON.parse(charBody).name;
            resolve(character);
          }
        });
      });
    });

    Promise.all(promises)
      .then((characters) => {
        characters.forEach((character) => {
          console.log(character);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
