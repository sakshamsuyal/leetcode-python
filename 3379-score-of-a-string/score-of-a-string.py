class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)-1):
             dif =  abs(ord(s[i])-ord(s[i+1]))
             total = total+dif
        return total
        