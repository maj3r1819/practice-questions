"""
Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""



def firstUniqChar( s: str) -> int:
    frequency = {}
    for c in s:
        if c not in frequency:
            frequency[c] = 1
        else:
            frequency[c] += 1

    print(frequency)

    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i
    return -1

print(firstUniqChar(s = "leetcode"))
