class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = 0
        window = set()
        for r in range(len(nums)):
            if nums[r] in window:
                return True
            else:
                window.add(nums[r])
            if r-l+1 > k:
                window.remove(nums[l])
                l+=1
        return False
               