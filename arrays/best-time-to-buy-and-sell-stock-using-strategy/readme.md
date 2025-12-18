# Best Time to Buy and Sell Stock using Strategy ✅

- **📁 Difficulty**  
  🟡 Medium

## Description

You are given two integer arrays `prices` and `strategy`, where:

- `prices[i]` is the price of a given stock on the `ith` day.
- `strategy[i]` represents a trading action on the `ith` day, where:
- `-1` indicates buying one unit of the stock.
- `0` indicates holding the stock.
- `1` indicates selling one unit of the stock.

You are also given an **even** integer `k`, and may perform **at most one** modification to `strategy`. A modification consists of:

- Selecting exactly `k` **consecutive** elements in `strategy`.
- Set the **first** `k / 2` elements to `0` (hold).
- Set the **last** `k / 2` elements to `1` (sell).

The **profit** is defined as the **sum** of `strategy[i] * prices[i]` across all days.

Return the **maximum** possible profit you can achieve.

**Note:** There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

### Example 1:

> Input: prices = [4,2,8], strategy = [-1,0,1], k = 2

> Output: 10

**Explanation:**

The maximum possible profit is 10, which is achieved by modifying the subarray `[0, 1]`.

- **Original Strategy:** `[-1, 0, 1]`. Profit: `(-1 * 4) + (0 * 2) + (1 * 8) = 4`.
- **Modify [0, 1]:** New Strategy `[0, 1, 1]`. Profit: `(0 * 4) + (1 * 2) + (1 * 8) = 10`.
- **Modify [1, 2]:** New Strategy `[-1, 0, 1]`. Profit: `(-1 * 4) + (0 * 2) + (1 * 8) = 4`.

### Example 2:

> Input: prices = [5,4,3], strategy = [1,1,0], k = 2

> Output: 9

**Explanation:**

The maximum possible profit is 9, which is achieved without any modification.

- **Original Strategy:** `[1, 1, 0]`. Profit: `(1 * 5) + (1 * 4) + (0 * 3) = 9`.
- **Modify [0, 1]:** New Strategy `[0, 1, 0]`. Profit: `(0 * 5) + (1 * 4) + (0 * 3) = 4`.
- **Modify [1, 2]:** New Strategy `[1, 0, 1]`. Profit: `(1 * 5) + (0 * 4) + (1 * 3) = 8`.

### Constraints:

- 2 <= prices.length == strategy.length <= 10^5
- 1 <= prices[i] <= 10^5
- -1 <= strategy[i] <= 1
- 2 <= k <= prices.length
- k is even

## Topics:

- Array
- Sliding Window
- Prefix Sum

## Solution

- **Space complexity:**
- O(n)

- **Time complexity:**
- O(n)

```python
from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
      def getProfit(prices: List[int], strategy: List[int]) -> int:
        n = len(prices)
        profit = []
        for i in range(0, n):
          profit.append(strategy[i] * prices[i])

        return profit

      n = len(prices)
      maxSeg = n +1 - (k)
      baseProfit = getProfit(prices, strategy)
      baseProfitSum = sum(baseProfit)
      maxProfit = baseProfitSum
      slice = math.floor(k/2)
      index = 0
      baseProfitWindow = 0
      modifiedProfitSeg = []
      modifiedProfitWindow = 0

      for seg in range(0,maxSeg):
        if seg == 0:
          baseProfitWindow = sum(baseProfit[index:k+index])
          modifiedProfitSeg = prices[index+slice:k+index]
          modifiedProfitWindow = sum(modifiedProfitSeg)
        else:
          baseProfitWindow = baseProfitWindow - baseProfit[index -1] + baseProfit[k+index -1]
          modifiedProfitWindow = modifiedProfitWindow - prices[index+slice -1] + prices[k+index -1]

        maxProfit = max(maxProfit, baseProfitSum - baseProfitWindow + modifiedProfitWindow)

        index+= 1


      return maxProfit

```
