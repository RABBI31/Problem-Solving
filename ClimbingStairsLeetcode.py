class Solution:
    def climbStairs(self, n: int) -> int:
        firstStep, secondStep = 0, 1
        for i in range(1, n+1):
            firstStep, secondStep = secondStep,secondStep+firstStep
        return secondStep
        