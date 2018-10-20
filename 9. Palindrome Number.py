class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # thought 1: convert the int to a string, and then compare each char. O(n) time, O(n) space.
        # thought 2: make an array, and store each digit to the array, and then compare each digit(check non-negative first). O(n) time, O(n) space.
        # thought 3: use a for loop to get the digit num, then compare the digit from each end(check non-negative first). O(n) time, O(1) space.
        # thought 4: convert x to reversed int y, and compare x and y(check non-negative and last digit not zero). [Wrong! the reversed int can be overflowed]
        # thought by answer: convert half of x to y and compare a and y.

        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        y = 0
        while x > y:
            y = y * 10 + x % 10
            x /= 10

        if x == y or x == y / 10:
            return True
        return False

# test
print Solution().isPalindrome(0)
print Solution().isPalindrome(10)
print Solution().isPalindrome(-5)
print Solution().isPalindrome(121)
print Solution().isPalindrome(666666)
