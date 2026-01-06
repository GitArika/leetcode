# Longest Substring Without Repeating Characters ✅

* **📁 Dificuldade**
🟡 Medium

## Description

Given a string `s`, find the length of the **longest substring** without duplicate characters.

### Example 1:

> **Input:** s = "abcabcbb"
> **Output:** 3
> **Explanation:** The answer is "abc", with the length of 3.

### Example 2:

> **Input:** s = "bbbbb"
> **Output:** 1
> **Explanation:** The answer is "b", with the length of 1.

### Example 3:

> **Input:** s = "pwwkew"
> **Output:** 3
> **Explanation:** The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints:

* 
* `s` consists of English letters, digits, symbols and spaces.

## Topics:

* Hash Table
* String
* Sliding Window

### Implementação (Python)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        longest = 0
        m = {}

        for windowEnd in range(len(s)):
            char = s[windowEnd]
            if char in m:
                windowStart = max(m[char] +1, windowStart)

            m[char] = windowEnd
            longest = max(longest, windowEnd - windowStart + 1)

        return longest
```

