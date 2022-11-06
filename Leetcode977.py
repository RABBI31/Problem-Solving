class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq=[i**2 for i in nums]
        dis = sorted(sq, key = int)
        return dis
            