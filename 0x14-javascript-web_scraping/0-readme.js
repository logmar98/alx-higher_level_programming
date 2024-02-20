#!/usr/bin/node
const fs = require('fs');

function printContent (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (err) {
    console.error(err);
  }
}
const filePath = process.argv[2];

printContent(filePath);
