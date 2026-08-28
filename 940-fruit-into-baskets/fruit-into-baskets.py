class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = 0
        window = dict()
        best = 0
        for r in range(len(fruits)):
            window[fruits[r]] = window.get(fruits[r],0)+1
            while len(window)>2:
              window[fruits[l]] -=1
              if window[fruits[l]] == 0:
                del window[fruits[l]]
              l+=1
             
            best = max(best,r-l+1)
        return best
