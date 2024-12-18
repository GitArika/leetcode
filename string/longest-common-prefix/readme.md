# Longest Common Prefix ✅
- **📁 Difficulty**  
  🟢 Easy 

## Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### Example 1:

> Input: strs = ["flower","flow","flight"]

> Output: "fl"

### Example 2:

> Input: strs = ["dog","racecar","car"]

> Output: ""

**Explanation:** There is no common prefix among the input strings.
 

### Constraints:

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.

## Topics
- String
- Trie

## Solution
- **Time Complexity:** 
  - O(n + m) where n is the number of strings and m is the length of the shortest string.
- **Space Complexity:** 
  - O(m)

```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix.append(chars[0])
            else:
                break

        return "".join(prefix)
```