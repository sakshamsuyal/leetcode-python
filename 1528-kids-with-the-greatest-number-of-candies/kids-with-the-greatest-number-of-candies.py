class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
       
        maximum = max(candies)
        result = []

        for candy in candies:
            result.append(candy + extraCandies >= maximum)

        return result