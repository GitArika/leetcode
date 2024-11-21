# Climbing Stairs ✅
- **📁 Difficulty**  
  🟢 Easy  

## 🔍 Description
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

### Example 1:

> Input: n = 2

> Output: 2

**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

### Example 2:

> Input: n = 3

> Output: 3

**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

### Constraints:

- 1 <= n <= 45

## Topics

- Math
- Dynamic Programming
- Memoization

## Solution
- **Time complexity:** 
  - O(n)
- **Space complexity:** 
  - O(n)

```ts
function climbStairs(n: number): number {
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
```
