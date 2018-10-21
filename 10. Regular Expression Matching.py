class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # answer: use dynamic programming, dp[i, j] returns if s[i:] and p[j:] match
        dict = {}
        def dp(i, j):
            if (i, j) not in dict:
                if p[j:] == "":
                    dict[i, j] = s[i:] == ""
                else:
                    first_match = s[i:] != "" and p[j] in {s[i], "."}
                    if j + 1 < len(p) and p[j+1] == "*":
                        dict[i, j] = dp(i, j+2) or (first_match and dp(i+1, j))
                    else:
                        dict[i, j] = first_match and dp(i+1, j+1)
            return dict[i, j]

        return dp(0, 0)


    def isMatchSlow(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # thought: recursively call isMatchSlow when we meet "*". Problem: slow!
        # i is the index of p, and j is the index of s
        # print "s:", s, "p:", p
        i, j = 0, 0
        while i < len(p):
            c = p[i]
            i += 1
            star = False
            if i < len(p) and p[i] == "*":
                i += 1
                star = True

            if c == ".":
                if star:
                    if self.isMatchSlow(s[j:], p[i:]):
                        return True
                    while j < len(s):
                        j += 1
                        if self.isMatchSlow(s[j:], p[i:]):
                            return True
                    return False
                else:
                    if j >= len(s):
                        return False
                    j += 1
            else:
                if star:
                    if self.isMatchSlow(s[j:], p[i:]):
                        return True
                    while j < len(s) and s[j] == c:
                        j += 1
                        if self.isMatchSlow(s[j:], p[i:]):
                            return True
                    return False
                else:
                    if j >= len(s) or s[j] != c:
                        return False
                    j += 1
        return j == len(s)


# test
print Solution().isMatch("banana", "ba")
print Solution().isMatch("banana", ".*nan")
print Solution().isMatch("banana", "bananana")
print Solution().isMatch("banana", ".*c")
print
print Solution().isMatch("banana", "banana")
print Solution().isMatch("banana", "......")
print Solution().isMatch("a", ".*")
print Solution().isMatch("banana", ".*")
print Solution().isMatch("banana", ".*banana")
print Solution().isMatch("banana", "b.*")
print Solution().isMatch("banana", "b.*a")
print Solution().isMatch("banana", "b.*a.*")
print Solution().isMatch("banana", "b.*an.")
print Solution().isMatch("banana", "b.*.*")
print Solution().isMatch("banana", "b.*a*")
print Solution().isMatch("aaaaa", "a.*a")