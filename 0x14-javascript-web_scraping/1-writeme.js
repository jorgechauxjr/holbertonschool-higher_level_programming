#!/usr/bin/node
const fs = require('fs');

const dataToWrite = process.argv[3];
const filePath = process.argv[2];

/* fs.writeFile(filePath, dataToWrite, 'utf8', function (err, data) { */
fs.writeFile(filePath, dataToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
