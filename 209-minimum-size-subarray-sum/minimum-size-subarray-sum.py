class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        window_sum = 0
        minu = float('inf')
        for r in range(len(nums)):
            window_sum += nums[r]
            while  window_sum >= target:
                minu = min(minu,r-l+1)
                window_sum -= nums[l]
                l+=1
        if minu == float('inf'):
            return 0
        else:
            return minu
            
            