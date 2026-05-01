class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefixSum = 0
        hashmap = {0: 1}  # important

        for num in nums:
            prefixSum += num
            
            if (prefixSum - k) in hashmap:
                count += hashmap[prefixSum - k]
            
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1
        
        return count