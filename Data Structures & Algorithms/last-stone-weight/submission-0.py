import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # by default a heap is a min heap

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            diff = abs(stone1) - abs(stone2)
            if diff != 0:
                heapq.heappush(stones, -1 * diff)
            
        
        if stones :
            return -1 * stones[0]
        else :
            return 0





        