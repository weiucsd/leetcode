class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # thought 1: for each char, check if its left and right are the same, O(n^2) time
        # note that, the palindrome can be "ABA" or "ABBA" format
        self.maxLen = 0
        self.output = ""
        for i in range(len(s)):
            # "ABA" format
            self.singleRound(s, i - 1, i + 1)
            # "ABBA" format
            self.singleRound(s, i, i + 1)
        return self.output

    def singleRound(self, s, left, right):
        currLen = right - left - 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            currLen += 2
        if currLen > self.maxLen:
            self.output = s[left + 1:right]
            self.maxLen = currLen
            
    def betterWay(self, s):
        self.maxLen = 0
        self.output = ""
        for i in range(len(s)):
            bias = max(1, self.maxLen/2)
            # "ABA" format
            self.betterRound(s, i - bias, i + bias)
            # "ABBA" format
            self.betterRound(s, i - bias + 1, i + bias)
        return self.output

    def betterRound(self, s, left, right):
        currLen = right - left - 1
        while left >= 0 and right < len(s) and s[left:right+1] == s[left:right+1][::-1]:
            left -= 1
            right += 1
            currLen += 2
        if currLen > self.maxLen:
            self.output = s[left + 1:right]
            self.maxLen = currLen

# test
print Solution().betterWay("babad")
print Solution().betterWay("cbbd")
print Solution().betterWay("a")
print Solution().betterWay("abcdefgfedcba")
print Solution().betterWay("")
print Solution().betterWay("eabcb")
print Solution().betterWay("abcdee")
print Solution().betterWay("ababababa")
print Solution().betterWay("ababa")
print Solution().betterWay("abb")
print Solution().betterWay("aaaabaaa")
print Solution().betterWay("dddddddd")
print Solution().betterWay("ddddddd")