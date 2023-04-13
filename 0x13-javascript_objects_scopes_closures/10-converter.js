#!/usr/bin/node

exports.converter = function (base) {
  return y => y.toString(base);
};
