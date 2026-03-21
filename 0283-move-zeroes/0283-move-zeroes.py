class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        for j in range(len(temp)):
            nums[j]=temp[j]
        nonzero=len(temp)
        for k in range(nonzero,len(nums)):
            nums[k]=0
        return nums
