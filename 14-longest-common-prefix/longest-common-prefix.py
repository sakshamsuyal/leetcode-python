class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""

        for j in range(min(len(each_string) for each_string in strs)):
            for i in range(len(strs)):
                if strs[i][j] != strs[0][j]:
                    return ans
            ans += strs[0][j]
        return ans
            
                