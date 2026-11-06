class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        for x in range(len(num)):
            if num[x] == '6':
               num[x] = '9'
               break
        return int(''.join(num))