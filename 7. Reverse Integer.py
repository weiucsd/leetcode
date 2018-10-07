class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        y = 0
        if x < 0:
            sign = -1
            x = -x
        while x > 0:
            y = 10 * y + x % 10
            x /= 10
        y = sign * y
        if y > 2**31-1 or y < -2**31:
            return 0
        return y

# test
print Solution().reverse(1)
print Solution().reverse(10)
print Solution().reverse(-1)
print Solution().reverse(123)
print Solution().reverse(120)
print Solution().reverse(-1998)
print Solution().reverse(0)
print 2<<30, Solution().reverse(2<<30)
print 2<<31, Solution().reverse(2<<31)
