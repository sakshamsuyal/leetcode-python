class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        for num in nums:
            s[num] = s.get(num,0)+1
        for x in s:
            if s[x]>len(nums)//2:
             return x
