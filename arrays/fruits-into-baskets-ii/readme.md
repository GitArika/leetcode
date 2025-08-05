# Fruits into Baskets II ✅

- **📁 Difficulty**  
  🟡 Medium

## Description

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where `fruits[i]` represents the quantity of the _i_-th type of fruit, and `baskets[j]` represents the capacity of the _j_-th basket.

From left to right, place the fruits according to these rules:

1. Each fruit type must be placed in the **leftmost available basket** with a capacity greater than or equal to the quantity of that fruit type.
2. Each basket can hold **only one type** of fruit.
3. If a fruit type cannot be placed in any basket, it remains unplaced.

Return the number of fruit types that remain unplaced after all possible allocations are made.

### Example 1:

> Input: fruits = [4,2,5], baskets = [3,5,4]  
> Output: 1

**Explanation:**

- fruits[0] = 4 is placed in baskets[1] = 5
- fruits[1] = 2 is placed in baskets[0] = 3
- fruits[2] = 5 cannot be placed in baskets[2] = 4  
  One fruit type remains unplaced → return 1.

---

### Example 2:

> Input: fruits = [3,6,1], baskets = [6,4,7]  
> Output: 0

**Explanation:**

- fruits[0] = 3 is placed in baskets[0] = 6
- fruits[1] = 6 skips baskets[1] = 4 (too small) and is placed in baskets[2] = 7
- fruits[2] = 1 is placed in baskets[1] = 4  
  All fruits are placed → return 0.

---

### Constraints:

- n == fruits.length == baskets.length
- 1 ≤ n ≤ 100
- 1 ≤ fruits[i], baskets[i] ≤ 1000

---

## Topics

- Array
- Simulation
- Greedy

---

## Hints

> The most straightforward approach is to simulate the placement exactly as described in the problem — iterate over each fruit, check each basket from left to right until you find one with enough capacity, and mark it as used.
>
> Since n ≤ 100, a simple O(n²) scan is efficient enough. However, for larger inputs, you can use a **segment tree** to find the leftmost valid basket in O(log n) per query, reducing the total complexity to O(n log n).

---

## Solution

- **Time complexity:** O(n²) — For each fruit, in the worst case, scan all baskets (O(n)) and remove one (O(n)).
- **Space complexity:** O(1) — Works in place, only a few extra variables.

```python
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        remaining = 0
        for i in range(len(fruits)):
            placed = False
            for basket in baskets:
                if basket >= fruits[i]:
                    baskets.remove(basket)  # remove used basket
                    placed = True
                    break
            if not placed:
                remaining += 1
        return remaining
```
