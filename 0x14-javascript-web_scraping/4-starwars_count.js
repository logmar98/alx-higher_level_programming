#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const charId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const filmsData = JSON.parse(body);

    const actorFilms = filmsData.results.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)
    );

    console.log(actorFilms.length);
  }
});
