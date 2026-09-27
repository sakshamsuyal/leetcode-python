class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        max_dep = 0
        for i in range(len(s)):
            if s[i] == '(':
                count+=1
            if s[i] == ')':
                count -=1
            max_dep = max(max_dep,count)
        return max_dep