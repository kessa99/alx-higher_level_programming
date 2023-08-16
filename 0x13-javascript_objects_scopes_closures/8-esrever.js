#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  for (let id = list.length - 1; id >= 0; id--) {
    newlist.push(list[id]);
  }
  return newlist;
};
