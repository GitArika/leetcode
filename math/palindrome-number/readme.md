# Palindrome Number ✅ 
- **📁 Difficulty**  
  🟢 Easy 

## Description 

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. 

### Example 1:

> Input: x = 121

> Output: true

**Explanation:** 121 reads as 121 from left to right and from right to left.

### Example 2:

> Input: x = -121

> Output: false

**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3:

> Input: x = 10

> Output: false

**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.
 
### Constraints:

- -231 <= x <= 231 - 1

## Topics
- Math

## Hint
> Beware of overflow when you reverse the integer.


## Solution
- **Time Complexity:**: O(log n)
- **Space Complexity:**: O(1)

```ts
function isPalindrome(x: number): boolean {
  if (x < 0 || (x % 10 === 0 && x !== 0)) {
    return false;
  }

  let reversed = 0;
  while (x > reversed) {
    reversed = (reversed * 10) + (x % 10);
    x = Math.floor(x / 10);
  }

  return x === reversed || x === Math.floor(reversed / 10);
}
```