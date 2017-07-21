class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(n) time complexity
        # O(n) space complexity
        dictionary = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in dictionary:
                dictionary[s[i]] += 1
            else:
                dictionary[s[i]] = 1
            if t[i] in dictionary:
                dictionary[t[i]] -= 1
            else:
                dictionary[t[i]] = -1
        for v in dictionary.values():
            if v != 0:
                return False
        return True
        
        '''
        # O(nlog(n)) time complexity
        s = sorted(s)
        t = sorted(t)
        
        if len(s) != len(t):
            return False
        return s == t
    
        '''
        
        '''
        # Brute Force using two dictionaries
        # O(n) time complexity
        
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
