class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0 
        r = 0
        while r<len(nums):
            if nums[r] == 0:
                r+=1
            else:
                nums[r], nums[l] = nums[l], nums[r]
                r+=1
                l+=1
            