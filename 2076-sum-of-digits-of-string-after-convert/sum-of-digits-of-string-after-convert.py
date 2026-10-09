class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        value = ""
        for i in range(len(s)):
            value += str(ord(s[i]) - ord('a') + 1 )
        while k>0:
            sum1 = 0
            for x in value:
               sum1 = sum1 + int(x)
            value = str(sum1)
            k-=1
        return int(value)

        