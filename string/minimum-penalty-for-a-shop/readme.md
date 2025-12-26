# Minimum Penalty for a Shop ✅

- **📁 Difficulty** 🟡 Medium

## Description

You are given the customer visit log of a shop represented by a 0-indexed string `customers` consisting only of characters `'N'` and `'Y'`:

- if the `ith` character is `'Y'`, it means that customers come at the `ith` hour
- whereas `'N'` indicates that no customers come at the `ith` hour.

If the shop closes at the `jth` hour (`0 <= j <= n`), the **penalty** is calculated as follows:

1. For every hour when the shop is open and no customers come, the penalty increases by 1.
2. For every hour when the shop is closed and customers come, the penalty increases by 1.

Return the **earliest** hour at which the shop must be closed to incur a **minimum** penalty.

_Note that if a shop closes at the `jth` hour, it means the shop is closed at the hour `j`._

### Example 1:

> Input: customers = "YYNY"

> Output: 2

**Explanation:**

- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
  Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

### Example 2:

> Input: customers = "NNNNN"

> Output: 0

**Explanation:** It is best to close the shop at the 0th hour as no customers arrive.

### Example 3:

> Input: customers = "YYYY"

> Output: 4

**Explanation:** It is best to close the shop at the 4th hour as customers arrive at each hour.

### Constraints:

- 1 <= `customers.length` <= 10^5
- `customers` consists only of characters `'Y'` and `'N'`.

## Topics

- String
- Prefix Sum
- Greedy

## Solution 1: Two Pass (Prefix/Suffix Logic)

This approach calculates the initial penalty assuming the shop never opens (sum of all 'Y's). Then, it iterates through the string updating the penalty: decrementing for 'Y' (customer served) and incrementing for 'N' (idle time).

- **Time Complexity:** - $O(N)$ (Iterates twice: once for counting 'Y', once for the loop)
- **Space Complexity:** - $O(1)$

```python
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Initial state: Shop closes at 0. Penalty is total count of 'Y's missed.
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        earliest_hour = 0

        for i, char in enumerate(customers):
            # If we stay open at hour i:
            if char == 'Y':
                # We served a customer we would have missed. Penalty drops.
                current_penalty -= 1
            else:
                # We stayed open for no one. Penalty increases.
                current_penalty += 1

            # Check if this new closing time (i + 1) is better
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                earliest_hour = i + 1

        return earliest_hour

```

## Solution 2: One Pass (Optimal Difference)

Instead of calculating the absolute penalty, we calculate a "score" (profit). We want to maximize the difference between customers served ('Y') and idle hours ('N'). This requires only a single pass and no pre-calculation.

- **Time Complexity:** - (Strictly one pass)
- **Space Complexity:** -

```python
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = 0
        current_score = 0
        best_hour = -1 # Represents closing at index 0 (technically before index 0)

        for i, customer in enumerate(customers):
            # 'Y' adds to score (good to be open), 'N' subtracts (bad to be open)
            current_score += 1 if customer == 'Y' else -1

            if current_score > max_score:
                max_score = current_score
                best_hour = i

        # The best closing hour is immediately after the best score index
        return best_hour + 1

```
