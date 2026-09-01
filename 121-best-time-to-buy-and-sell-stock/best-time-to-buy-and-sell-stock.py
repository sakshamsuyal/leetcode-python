class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        best = 0
        profit = 0
        r=l+1
        while( r<len(prices)):
            profit = prices[r]-prices[l]
            if prices[l]>=prices[r]:
                l=r
                r+=1
            elif(prices[l]<prices[r]):
                best = max(best,profit)
                r+=1
            
        return best

