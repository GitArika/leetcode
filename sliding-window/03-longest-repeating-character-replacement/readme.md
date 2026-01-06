
# 424. Longest Repeating Character Replacement ✅

* **📁 Dificuldade**
🟡 Medium

## Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Example 1:

> **Input:** s = "ABAB", k = 2
> **Output:** 4
> **Explanation:** Replace the two 'A's with two 'B's or vice versa.

### Example 2:

> **Input:** s = "AABABBA", k = 1
> **Output:** 4
> **Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.

### Constraints:

* `1 <= s.length <= 10^5`
* `s` consists of only uppercase English letters.
* `0 <= k <= s.length`

## Topics:

* Hash Table
* String
* Sliding Window

### Implementação (Python)

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        windowStart = 0
        mostFreq = 0
        m = {}

        for windowEnd in range(len(s)):
            char = s[windowEnd]
            # Atualiza frequência no mapa
            if char not in m:
                m[char] = 1
            else:
                m[char] += 1 
            
            # Mantém o registro do caractere mais frequente historicamente na janela
            if m[char] > mostFreq:
                mostFreq = m[char]

            # A janela é válida se: (tamanho total - freq do majoritário) <= k
            lettersToReplace = (windowEnd - windowStart + 1) - mostFreq 

            # Se exceder k, encolhemos a janela pela esquerda
            if lettersToReplace > k:
                m[s[windowStart]] -= 1
                windowStart += 1 
            
            # Atualiza o tamanho máximo encontrado
            longest = max(longest, windowEnd - windowStart + 1)
            
        return longest
```
