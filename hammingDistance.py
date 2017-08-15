class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        '''
        # O(n) time and O(n) space
        x = bin(x)
        new = bin(new)
        counter = 0
        for i in range(2,len(new)):
            if new[i] == '1':
                counter += 1
        return counter
    
        '''
        '''
        # O(n) time and O(1) space
        x = bin(x)
        counter = 0
        for i in range(2, len(x)):
            if x[i] == '1':
                counter += 1
        return counter
        '''
        
        # O(n) time and O(1) space
        counter = 0
        while x:
            x &= (x-1)
            counter += 1
        return counter
