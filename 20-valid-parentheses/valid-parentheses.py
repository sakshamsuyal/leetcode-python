class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = []
        pairs = {
                 ')': '(',
                 ']': '[',
                 '}': '{'
        }
        for char in s:
            if char in '([{':
                ans.append(char)
            elif char in  ")]}":
                if not ans:
                    return False
                if ans[-1] != pairs[char]:
                    return False
                if not  ans:
                    return False
                else:
                    ans.pop()
        return not ans
            