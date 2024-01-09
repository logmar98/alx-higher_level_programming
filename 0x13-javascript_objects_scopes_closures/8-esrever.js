#!/usr/bin/node
exports.esrever = function (list) {
  let lent = list.length - 1;
  let i = 0;
  while ((lent - i) > 0) {
    const tmp = list[lent];
    list[lent] = list[i];
    list[i] = tmp;
    i++;
    lent--;
  }
  return list;
};
