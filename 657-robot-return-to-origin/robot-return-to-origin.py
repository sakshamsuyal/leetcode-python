class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = 0
        pos1 = 0
        for i  in  range(len(moves)):
            if moves[i] == 'R':
                pos+=1
            elif moves[i] == 'L':
                pos-=1
            elif moves[i] == 'U':
                pos1+=1
            elif moves[i] == 'D':
                pos1-=1
        if pos == 0 and pos1 == 0:
            return  True
        else:
            return False
