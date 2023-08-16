#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let count = 0;
	for (let id = 0; id < list.length; id++) {
		if (list[id] === searchElement) {
			count++;
		}
	}
	return count;
};
