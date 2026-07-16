class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num
        while left<=right:
            middle=(left+right)//2
            if (middle*middle) == num:
             return True
            elif middle*middle < num:
             left = middle+1
            else:
             right = middle-1
        return False