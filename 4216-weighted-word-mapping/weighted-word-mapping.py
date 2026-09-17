class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        result = ""
        total = 0
        idk = []

        for i in words:
            for char in i:
                num = weights[ord(char) - ord('a')]
                total = num + total

            mod = total % 26
            idk.append(mod)
            total = 0

        for num in idk:
            result = result + chr(122-num)

        return result