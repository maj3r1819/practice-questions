"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while (1):
            if n in [0]:
                return False
            elif n % 3 == 0:
                n = n / 3
                if n == 1:
                    return True
            else:
                return False

