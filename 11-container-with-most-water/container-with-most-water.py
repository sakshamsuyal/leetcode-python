class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        a = 0
        while r>l:
            w = r-l
            current_area = w*min(height[l],height[r])
            a = max(a,current_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return a     