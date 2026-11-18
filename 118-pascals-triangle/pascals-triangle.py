class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        for _ in range(1,numRows):
           if numRows == 0:
              return []
           prev = triangle[-1]
           curr = [1]
           for i in range(len(prev)-1):
            curr.append(prev[i] + prev[i+1])

           curr.append(1)

           triangle.append(curr)
        return triangle