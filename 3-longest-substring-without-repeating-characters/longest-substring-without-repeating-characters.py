class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = set()
        best=0
        l =0
        for r in range(len(s)):
            if s[r] in window:
               while s[r] in window:
                  window.remove(s[l])
                  l+=1
            window.add(s[r])
            best = max(best,r-l+1)
        return best
