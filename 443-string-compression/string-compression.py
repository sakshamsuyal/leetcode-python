class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count = 1
        write = 0
        for i in range(len(chars)-1):
            if chars[i] == chars[i+1]:
                count+=1
            else:
                chars[write] = chars[i]
                write+=1
                if count>1:
                    for stim in str(count):
                     chars[write] = stim
                     write+=1
                count = 1
        
        chars[write] = chars[-1]
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
        return write

