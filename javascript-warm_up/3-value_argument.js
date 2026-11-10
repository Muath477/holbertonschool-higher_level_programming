#!/usr/bin/node
const first = process.argv[2];

if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
