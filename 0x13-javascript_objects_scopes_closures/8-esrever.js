#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  /* iterating over the elements of
  the input array in reverse order */
  for (let i = list.length - 1; i >= 0; i--) {
    // finally reversed array.
    reversed.push(list[i]);
  }
  return reversed;
};
