/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
  let index = digits.length - 1

  if (digits[index] === 9) {
    while (digits[index] === 9 && index !== 0) {
      digits[index] = 0

      index--;
    }

    if (digits[index] === 9) {
      digits[index] = 0;
      digits.unshift(1)
    } else {
      digits[index] = digits[index] + 1;
    }
  } else {
    digits[index] = digits[index] + 1;
  }

  return digits;
};