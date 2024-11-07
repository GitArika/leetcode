# Plus One ✅
- **📁 Difficulty**  
  🟢 Easy  

## 🔍 Description

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`'s.

Increment the large integer by one and return the _resulting array of digits._

### Example 1:

> Input: digits = [1,2,3]

> Output: [1,2,4]

**Explanation:** 
- The array represents the integer 123.
- Incrementing by one gives 123 + 1 = 124.
- Thus, the result should be [1,2,4].

### Example 2:

> Input: digits = [4,3,2,1]

> Output: [4,3,2,2]

**Explanation:** 
- The array represents the integer 4321.
- Incrementing by one gives 4321 + 1 = 4322.
- Thus, the result should be [4,3,2,2].

### Example 3:

> Input: digits = [9]

> Output: [1,0]

**Explanation:** 
- The array represents the integer 9.
- Incrementing by one gives 9 + 1 = 10.
- Thus, the result should be [1,0].
 
### Constraints:

- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.

## Topics
- Array
- Math

## Solution
- **Time Complexity:** 
  - O(n)
- **Space Complexity:** 
  - O(1)
  - O(n) worst case (e.g., [9, 9, 9])

```js
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    if (digits[i] < 9) {
      digits[i] += 1;
      return digits;
    }
    digits[i] = 0; // Set to 0 if it's 9 and continue
  }

  // If all digits were 9, we end up with 0s; prepend 1 at the start.
  digits.unshift(1);
  return digits;
};
```