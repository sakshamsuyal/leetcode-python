class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l = 0
        window_sum = 0
        best = float('-inf')
        for r in range(len(nums)):
            window_sum += nums[r]
            if r-l+1>k:
             window_sum -= nums[l]
             l+=1
            if r-l+1==k:
             best = max(best, window_sum)
        return float(best)/k