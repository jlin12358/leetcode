class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        '''
        # O(n) time and O(n) space
        num = bin(num)[2:]
        s = ""
        for i in range(len(num)):
            if num[i] == '0':
                s += '1'
            else:
                s += '0'
        return int(s, 2)
        '''
        
        '''
        # O(n) time and O(1) space
        num = list(bin(num)[2:])
        for i in range(len(num)):
            if num[i] == '0':
                num[i] = '1'
            else:
                num[i] = '0'
        return int(str(num), 2)
        '''
        # O(logn) time O(1) space
        two = 1
        while two <= num:
            two *= 2
        return num ^ (two-1)
