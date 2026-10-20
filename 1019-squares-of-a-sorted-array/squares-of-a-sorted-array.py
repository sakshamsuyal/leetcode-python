class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        pos = len(nums) - 1
        left = 0
        right = len(nums) - 1

        while left <= right:
            i = nums[left] * nums[left]
            x = nums[right] * nums[right]

            if i >= x:
                ans[pos] = i
                left += 1
            else:
                ans[pos] = x
                right -= 1

            pos -= 1

        return ans

         