class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        r = 0
        l = 0
        while r<len(s) and l<len(t):
            if s[r]==t[l]:
                r+=1
                l+=1
            else:
                l+=1
        if r == len(s):
            return True
        else:
            return False