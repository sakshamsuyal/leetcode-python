class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters)-1
        while left<=right:
            middle = (left+right)//2
            if letters[middle] <= target:
                left = middle+1
            else:
                right = middle -1
        if left == len(letters):
           return letters[0]
        return letters[left]