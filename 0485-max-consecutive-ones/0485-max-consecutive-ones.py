class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        currentcount=0
        for i in range(len(nums)):
            if(nums[i]==0):
                currentcount=0
            else:
                currentcount+=1

            if(currentcount>ans):
                ans=currentcount

        return ans
        
        