class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        S = set(nums1)
        for i in S:
         if i in nums2:
            ans.append(i)
        return ans