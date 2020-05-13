#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntilles = '18'; /* 18 is Id for the character wedge antilles */

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let numMovies = 0;
    for (const movieInfo in results) {
      const characters = results[movieInfo].characters;
      for (const idCharacter in characters) {
        if (characters[idCharacter].includes(wedgeAntilles)) {
          numMovies++;
        }
      }
    }
    console.log(numMovies);
  }
});
