var climbStairs = function (n) {
  let counts = new Array(n + 1).fill(0);
  counts[0] = 1;

  for (let i = 1; i <= n; i++) {
    counts[i] += counts[i - 1];
    if (i - 2 >= 0) {
      counts[i] += counts[i - 2];
    }
  }

  return counts[n];
};