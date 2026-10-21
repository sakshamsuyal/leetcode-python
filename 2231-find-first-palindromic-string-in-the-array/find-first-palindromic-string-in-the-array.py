class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for char in words:
            inv = char[::-1]
            if char == inv:
                return char
        return ""
