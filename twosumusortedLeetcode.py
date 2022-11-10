class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in arr: return [arr[r], i]
            arr[j] = i
        