class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        right  = 0
        left = len(nums)-1
        index = len(nums) - 1
        answer = [0]*len(nums)
        while left>=right:
            if nums[right]*nums[right] < nums[left]*nums[left]:
                answer[index] = nums[left]*nums[left]
                left-=1
            else:
                answer[index] = nums[right]*nums[right]
                right += 1

            index -= 1
        return answer   