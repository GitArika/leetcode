# 1004. Max Consecutive Ones III ✅

* **📁 Dificuldade**
🟡 Medium

## Description

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.

### Example 1:

> **Input:** nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
> **Output:** 6
> **Explanation:** [1,1,1,0,0,**1**,**1**,1,1,1,1]
> Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

### Example 2:

> **Input:** nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
> **Output:** 10
> **Explanation:** [0,0,1,1,**1**,**1**,1,1,1,1,1,1,0,0,0,1,1,1,1]

### Constraints:

* `1 <= nums.length <= 10^5`
* `nums[i]` is either `0` or `1`.
* `0 <= k <= nums.length`

## Topics:

* Array
* Binary Search
* Sliding Window
* Prefix Sum

### Implementação (Python)

```python
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0 
        n = len(nums)

        for windowEnd in range(n):
            # Se encontramos um 0, "gastamos" uma operação de flip
            if nums[windowEnd] == 0:
                k -= 1

            # Se k < 0, a janela é inválida (usamos mais flips que o permitido)
            # Movemos o início da janela para recuperar o crédito de k se necessário
            if k < 0:
                if nums[windowStart] == 0:
                    k += 1
                windowStart += 1
        
        # O tamanho da maior janela válida encontrada é mantido implicitamente
        return n - windowStart

```
