class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        right = m - 1
        left = n - 1
        idk = m + n - 1

        answer = [0] * (m + n)

        while left >= 0 and right >= 0:
            if nums1[right] > nums2[left]:
                answer[idk] = nums1[right]
                right -= 1
            elif nums2[left] > nums1[right]:
                answer[idk] = nums2[left]
                left -= 1
            else:
                answer[idk] = nums1[right]
                right -= 1
            idk -= 1

        while right >= 0:
            answer[idk] = nums1[right]
            right -= 1
            idk -= 1

        while left >= 0:
            answer[idk] = nums2[left]
            left -= 1
            idk -= 1

        for i in range(m + n):
            nums1[i] = answer[i]