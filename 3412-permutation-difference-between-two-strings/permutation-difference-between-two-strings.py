class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        total = 0
        for i,char in enumerate(s):
            j = t.index(char)
            total += abs(j-i)
        return total