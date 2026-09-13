class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        s = set(nums1)
        b = set(nums2)
        ans1 = []
        ans2 = []
        for x in s:
            if x not in b:
                ans1.append(x)
        for y in b:
            if y not in s:
                ans2.append(y)
        return [ans1, ans2]

