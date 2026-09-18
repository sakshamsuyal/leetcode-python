class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>1:
         ans  = self.fib(n-1)+ self.fib(n-2)
         return ans
        else:
            return n