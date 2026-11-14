class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            x = i+1
            y = i+2
            if nums[x]+nums[y]>nums[i]:
              z = nums[x]+nums[y]+nums[i]
              return z 
        return 0
