class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for x in alphabet:
            if x  not in sentence:
                return False
        return True

        