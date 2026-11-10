#!/usr/bin/node
function factorial (n) {
  // NaN (no argument or not a number) counts as 1, like 0! and 1!
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(parseInt(process.argv[2])));
