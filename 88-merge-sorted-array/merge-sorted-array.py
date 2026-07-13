class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        final = nums1[:m]+nums2[:n]
        for i in range(1,len(final)):
            current = final[i]
            j = i-1
            while j>=0 and final[j] >current:
                final[j+1] = final[j]
                j = j-1
            final[j+1] = current
        nums1[:] = final
       