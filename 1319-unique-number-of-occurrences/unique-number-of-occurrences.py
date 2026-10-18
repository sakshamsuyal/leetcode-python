class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for num in arr:
            freq[num] = freq.get(num,0)+1
        count = set(freq.values())
        if len(freq.values()) == len(set(freq.values())):
            return True
        return False
