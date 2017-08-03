class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        '''
        # O(n) time and O(n) space
        l = s.split()
        for i in range(len(l)):
            l[i] = l[i][::-1]
        for each in l:
            s += each
            s += ' '
        return s[:-1]
        '''
        
        # O(n) time and O(1) space
        if s == "":
            return ""
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        
        return reduce(lambda x, y: x + ' ' + y, s)        

