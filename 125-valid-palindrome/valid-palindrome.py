class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        lower =  s.lower()
        while left<right:
            if not lower[left].isalnum():
                left+=1
                continue
            if not lower[right].isalnum():
                right-=1
                continue
            if lower[left] != lower[right]:
                return False
            left+=1
            right-=1
            
        return True
            