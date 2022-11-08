#seen
i = 0
j=1
while j < len(nums):
        #print("i : " + str(i) + " j : " + str(j))
        if nums[i] == 0 and nums[j] != 0:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j += 1
        elif nums[i] != 0:
            i += 1
            j += 1
        else:
            j +=1
#mysolution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num = sorted(nums)
        count = 0;
        for i in range(len(num)):
            if(num[i]==0):
                count +=1
        while count > 0:
            num.insert(len(num)-1,num.pop(0))
            count -= 1