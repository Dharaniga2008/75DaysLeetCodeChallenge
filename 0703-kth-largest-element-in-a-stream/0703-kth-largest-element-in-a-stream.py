import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        # Convert list into min heap
        heapq.heapify(self.heap)

        # Keep only k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        
        # Add new value
        heapq.heappush(self.heap, val)

        # Remove smallest if heap size exceeds k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # kth largest element
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)