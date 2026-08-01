class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        r = 0
        l = 0
        ans = []
        while r<len(s) and l<len(t):
            if s[r]==t[l]:
                ans.append(t[l])
                r+=1
                l+=1
            else:
                l+=1
        ans = "".join(ans)
        if ans == s:
            return True 
        else:
            return False