class Solution:
    #remove duplicates from array
    def removeDuplicates(self, nums: List[int]) -> int:
        a=0
        for b in range(1,len(nums)):
            if nums[b] != nums[a]:
                nums[a+1] = nums[b]
                a+=1
        return a+1
        