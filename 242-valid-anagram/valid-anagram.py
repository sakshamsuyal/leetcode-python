class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count1 = {}
        count2 = {}
        for c in s:
            count1[c] = count1.get(c,0)+1
        for c in t:
            count2[c] = count2.get(c,0)+1
        return count1 == count2