class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count1 = 0
        count2 = 0
        vow = 'aeiouAEIOU'
        mid = len(s)/2
        first  = s[:mid]
        last = s[mid:]
        for i in first:
             if i in vow:
                count1 +=1
        for y in last:
            if y in vow:
              count2 +=1
        return count1 == count2