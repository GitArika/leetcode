/**
 * @param {string} s
 * @return {number}
 */
var minLength = function (s) {
  while (/AB|CD/g.test(s)) {
    s = s.replace(/AB|CD/g, '')
  }

  return s.length
};