class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # O(n) time - creation of the set
        # O(1) space
        
        return min(len(frozenset(candies)), len(candies)/2)
        
        '''
        # O(n^2) time  : 1 for loop and "in" function
        # O(n)   space
        count = 0
        seen = {}
        for each in candies:
            if each not in seen:
                seen[each] = 1
                count += 1
            if count >= len(candies)/2:
                return len(candies)/2
        return count
        '''
