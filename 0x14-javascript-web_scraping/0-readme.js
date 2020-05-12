#!/usr/bin/node

const fs = require('fs');

/* Otra fforma linea 7 fs.readFile(process.argv[2], 'utf-8', function (err, data) { */
/* posicion 2 es el 1er argumento. pos 0 y 1 estan usados */

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
