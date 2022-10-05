#!/usr/bin/node

exports.callMeMoby = (x, func) => {
  while (x > 0) {
    func();
    x--;
  }
};
