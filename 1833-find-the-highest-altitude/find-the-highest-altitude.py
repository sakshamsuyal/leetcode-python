class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        high = 0
        best = 0
        for i in range(len(gain)):
            high = high+gain[i]
            best = max(best,high)
        return best