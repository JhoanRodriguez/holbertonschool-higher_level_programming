#!/usr/bin/node
/* Script that counts the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  const listLength = list.length;

  for (let i = 0; i < listLength; i++) {
    if (list[i] === searchElement) { counter++; }
  }

  return counter;
};
