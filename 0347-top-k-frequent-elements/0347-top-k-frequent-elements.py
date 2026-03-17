class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(sorted_items[i][0])
        return result


        