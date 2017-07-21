class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # O(nlog(n)) time complexity
        s = sorted(s)
        t = sorted(t)
        
        if len(s) != len(t):
            return False
        return s == t
    
        '''
        # Brute Force using two dictionaries
        # O(n^2) time complexity
        
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        for each in s:
            if dict_t[each] != dict_s[each]:
                return False
        return True
        '''
