class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = 0
        idk = dict()
        s1_dict = {}
        for ch in s1:
            s1_dict[ch] = s1_dict.get(ch, 0) + 1
        for r in range(len(s2)):
            idk[s2[r]] = idk.get(s2[r],0)+1
            while r-l+1>len(s1):
                idk[s2[l]] -=1
                if idk[s2[l]] == 0:
                 del idk[s2[l]]
                l+=1
            if r-l+1 == len(s1):
                if idk == s1_dict:
                    return True
        
        return False