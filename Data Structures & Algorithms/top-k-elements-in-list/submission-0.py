import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        
        heap = []
        for num in hmap.keys(): # Count of each number as hmap value
            heapq.heappush(heap, (hmap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        for index in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        
        