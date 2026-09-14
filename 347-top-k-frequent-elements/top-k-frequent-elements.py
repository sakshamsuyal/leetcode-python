class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num  in nums:
            idk =freq.get(num, 0)
            idk+=1
            freq[num] = idk
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_freq[:k]]
