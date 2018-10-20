class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = 0
        sign = 0
        start = False
        for i in range(len(str)):
            if str[i] == ' ':
                if start:
                    break
            elif str[i] == '+':
                if start:
                    break
                sign = 1
                start = True
            elif str[i] == '-':
                if start:
                    break
                sign = -1
                start = True
            elif str[i] >= '0' and str[i] <= '9':
                num = num * 10 + ord(str[i]) - ord('0')
                start = True
            else:
                break
        if sign == -1:
            num = -num

        if num > 2**31-1:
            return 2**31-1
        if num < -2**31:
            return -2**31
        return num

# test
print Solution().myAtoi("42")
print Solution().myAtoi("   -42")
print Solution().myAtoi("4193 with words")
print Solution().myAtoi("words and 987")
print Solution().myAtoi("-91283472332")
print Solution().myAtoi("   +0 123")
print Solution().myAtoi("-   234")
print Solution().myAtoi("0-1")