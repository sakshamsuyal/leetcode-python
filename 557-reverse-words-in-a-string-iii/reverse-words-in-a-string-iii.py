class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.split()
        ans = []
        for char in  x:
            ans.append(char[::-1])
        return " ".join(ans)
            

        