class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        best = 0
        count = 0
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                count+=1
            elif nums[i+1] - nums[i] > 1:
                count = 0
            best = max(best,count)
        return best+1
