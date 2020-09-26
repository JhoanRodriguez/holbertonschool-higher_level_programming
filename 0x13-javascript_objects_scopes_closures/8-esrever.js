#!/usr/bin/node
/*  function that returns the reversed version of a list */
exports.esrever = function (list) {
  let swap = null;
  const listLength = list.length;
  let j = listLength - 1;

  for (let i = 0; i < j; i++) {
    swap = list[i];
    list[i] = list[j];
    list[j] = swap;
    j--;
  }
  return list;
};
