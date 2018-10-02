class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # thought: for each char, calculate which row it belongs to, loop in 2*n-2
        # note: did not consider n==1 at first
        if numRows == 1:
            return s
        rows = [[]for _ in range(numRows)]
        for i in range(len(s)):
            id = i % (2*numRows-2)
            if id >= numRows:
                id = 2*numRows-2-id
            rows[id].append(s[i])

        output = ""
        for row in rows:
            for c in row:
                output += c
        return output

# test
print Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
print Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
print Solution().convert("", 4) == ""
print Solution().convert("abc", 4) == "abc"
print Solution().convert("A", 1) == "A"
print Solution().convert("AB", 1) == "AB"
print Solution().convert("AB", 2) == "AB"