class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(nlog(n)) time O(1) space
        nums = sorted(nums)
        c = 0
        for i in range(len(nums)/2):
            c += min(nums[(i*2)], nums[(i*2) + 1])
        return c
