/**
 * https://leetcode.com/problems/maximum-swap/description/
 * @param {number} num
 * @return {number}
 */
var maximumSwap = function (num) {
  let snum = String(num);
  for (let i = 0; i < snum.length; i++) {
    let max = [-1, 0];
    for (let j = snum.length; j > i; j--) {
      if (Number(max[0]) < Number(snum[j])) {
        max = [snum[j], j];
      }
    }

    if (Number(snum[i]) < Number(max[0])) {
      let aux = snum.split('')
      let swap = aux[i]
      aux[i] = max[0];
      aux[max[1]] = swap;
      return Number(aux.join().replaceAll(',', ''));
    }
  }

  return num;
};