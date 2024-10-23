/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  const re = new RegExp(needle);
  return haystack.search(re);
};