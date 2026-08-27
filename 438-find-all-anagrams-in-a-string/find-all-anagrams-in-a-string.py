class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l = 0
        window = dict()
        p_dict = {}
        result = []
        for ch in p:
            p_dict[ch] = p_dict.get(ch,0)+1
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            while r-l+1 > len(p):
                window[s[l]] -=1
                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1
            if r-l+1 == len(p):
                if window == p_dict:
                    result.append(l)
        return result