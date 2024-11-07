# Maximum Swap ✅
- **📁 Difficulty**  
  🟢 Easy  

## Companies
You are given an integer `num`. You can swap two digits at most once to get the maximum valued number.

Return the _maximum valued number_ you can get.

### Example 1:

> Input: num = 2736

> Output: 7236

**Explanation:** 
- Swap the number 2 and the number 7.

### Example 2:

> Input: num = 9973

> Output: 9973

**Explanation:** 
- No swap.
 
### Constraints:

- 0 <= num <= 108

## Topics
- Math
- Greedy

## Solution
- **Time Complexity:** 
  - O(n)
- **Space Complexity:** 
  - O(n)

```js
/**
 * @param {number} num
 * @return {number}
 */
var maximumSwap = function(num) {
  const snum = String(num).split('');
  const lastPosition = Array(10).fill(-1);

  // Record the last occurrence of each digit
  for (let i = 0; i < snum.length; i++) {
    lastPosition[+snum[i]] = i;
  }

  // Try to find the first position to swap
  for (let i = 0; i < snum.length; i++) {
    for (let d = 9; d > +snum[i]; d--) {
      if (lastPosition[d] > i) { // If a larger digit exists later
        // Swap the current digit with the larger one
        [snum[i], snum[lastPosition[d]]] = [snum[lastPosition[d]], snum[i]];
        return Number(snum.join(''));
      }
    }
  }

  return num;
};
```