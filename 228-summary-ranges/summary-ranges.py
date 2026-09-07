class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start = 0
        ans = []

        for i in range(len(nums) - 1):
            b = i + 1

            if nums[b] - nums[i] == 1:
                continue

            elif nums[b] - nums[i] != 1:
                if start == i:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[i]))

                start = i + 1

        if len(nums) > 0:
            if start == len(nums) - 1:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start]) + "->" + str(nums[-1]))
        return ans