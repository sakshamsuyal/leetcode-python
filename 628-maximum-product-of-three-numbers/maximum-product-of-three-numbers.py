class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        smallest = float('inf')
        second_smallest = float('inf')
        for num in nums:
            if num>first:
               third = second
               second = first
               first = num
            elif num>second:
                third = second
                second = num
            elif num>third:
                third = num
            
            if num<smallest:
                second_smallest = smallest
                smallest = num
            elif num<second_smallest:
                second_smallest = num
        return max(first * second * third,
           smallest * second_smallest * first)
    