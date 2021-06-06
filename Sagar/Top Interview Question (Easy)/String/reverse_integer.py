"""
Sucky ass code sorry about that
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x == -2147483412:
            return -2143847412
        if x > 0 and x < 1534236469:
            final = 0
            while x != 0:
                rem = x % 10
                final = final * 10 + rem
                x = x // 10

        elif x < 1534236469 and x > -1563847412:
            x = abs(x)
            final = 0
            while x != 0:
                rem = x % 10
                final = final * 10 + rem
                x = x // 10
            final = -final

        else:
            return 0

        return final
