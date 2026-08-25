class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0 
        count = 0
        best = 0
        for r in range(len(s)):
            if s[r] in 'aeiou':
                count+=1
            if r-l+1 > k:
              if s[l] in 'aeiou':
                count -=1
              l +=1
            if r-l+1 == k:
              best = max(best,count)
        return best