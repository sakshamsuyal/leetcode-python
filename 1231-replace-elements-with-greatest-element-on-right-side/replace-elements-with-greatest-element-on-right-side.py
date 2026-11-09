class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = [0]*len(arr)
        maximum = -1
        for i in range(len(arr)-1,-1,-1):
            result[i] = maximum
            maximum = max(maximum,arr[i])
        return result