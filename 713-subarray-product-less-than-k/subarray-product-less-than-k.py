class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        l = 0
        product = 1
        count = 0
        for r in range(len(nums)):
            product *= nums[r]
            while l <= r  and  product >=k :
                product //= nums[l]
                l+=1
            if product <k:
                count += r-l+1
        return count
            

