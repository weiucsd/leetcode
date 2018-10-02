class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # thought 1: for each char as a start, seek the longest substring, O(n^2) time
        # thought 2: use a map to record current substring's chars, use two pointer to record the start and end

        i, j = 0, 0
        substring = {}
        maxLen = 0
        for i in range(len(s)):
            while j < len(s) and s[j] not in substring:
                substring[s[j]] = j
                j += 1
            maxLen = max(maxLen, j - i)
            substring.pop(s[i])
        return maxLen

# test
print Solution().lengthOfLongestSubstring("abcabcbb")
print Solution().lengthOfLongestSubstring("bbbb")
print Solution().lengthOfLongestSubstring("pwwkew")
print Solution().lengthOfLongestSubstring("")
print Solution().lengthOfLongestSubstring("a")