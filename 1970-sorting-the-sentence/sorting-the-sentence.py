class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        ans = [""] * len(words)

        for word in words:
            pos = int(word[-1])
            ans[pos - 1] = word[:-1]

        return " ".join(ans)