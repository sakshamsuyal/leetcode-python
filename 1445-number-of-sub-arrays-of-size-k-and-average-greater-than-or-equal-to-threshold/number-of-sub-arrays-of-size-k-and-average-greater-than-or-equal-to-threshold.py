class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        l = 0
        window_sum = 0
        count = 0
        for  r in  range(len(arr)):
            window_sum += arr[r]
            if r-l+1>k:
               window_sum -= arr[l]
               l+=1
            if r-l+1 == k:
               if window_sum >= threshold*k:
                 count+=1
        return count      
            