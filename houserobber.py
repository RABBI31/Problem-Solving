class Solution:
    def rob(self, nums: List[int]) -> int:
        sums = (0,0)
        for i in nums:
            sums = (sums[1] ,max(sums[0]+i, sums[1]))
        return sums[1]