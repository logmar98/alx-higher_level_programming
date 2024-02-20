#!/usr/bin/node
const fs = require('fs');

function writeContent (filePath, fileText) {
  try {
    fs.writeFileSync(filePath, fileText, 'utf-8');
  } catch (err) {
    console.error(err);
  }
}
const filePath = process.argv[2];
const fileText = process.argv[3];

writeContent(filePath, fileText);
