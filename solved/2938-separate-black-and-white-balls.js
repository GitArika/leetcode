/**
 * https://leetcode.com/problems/separate-black-and-white-balls/description/
 * @param {string} s
 * @return {number}
 */
var minimumSteps = function (s) {
  let ac = 0, swap = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] == '0') ac++;
    else swap += ac;
  }
  return swap;
};