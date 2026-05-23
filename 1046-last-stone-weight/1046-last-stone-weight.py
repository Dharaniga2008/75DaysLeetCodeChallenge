import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Python has min heap, so use negative values for max heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        # Keep smashing until one or no stone is left
        while len(stones) > 1:

            # Take two heaviest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # If they are different, push the remaining weight
            if first != second:
                heapq.heappush(stones, -(first - second))

        # If one stone remains, return it
        return -stones[0] if stones else 0