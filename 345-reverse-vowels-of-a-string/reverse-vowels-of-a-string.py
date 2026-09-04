class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'aeiou'
        lower = s.lower()
        l = 0
        r = len(s)-1
        char = list(s)
        while l<r:
          if lower[l] not in vowel:
            l+=1
          elif lower[r] not in vowel:
            r-=1
          else:
            char[l],char[r] = char[r],char[l]
            l+=1
            r-=1
        return ''.join(char)
