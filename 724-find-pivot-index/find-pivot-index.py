class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            left = nums[0:i]
            right = nums[i+1:len(nums)]
            lsum = sum(left)
            rsum = sum(right)
            if lsum == rsum:
                return i
            
        return -1
            
