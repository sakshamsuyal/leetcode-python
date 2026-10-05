class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        word = ""
        for y in words:
         word += y[0]
        if word == s:
            return True
        else:
            return False        