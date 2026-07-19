import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            if num in hmap :
                hmap[num] += 1
            else :
                hmap[num] = 1
        
        max_heap = [] # By default a heapq heappush - gives minheap  
        for key, value in hmap.items():
            heapq.heappush(max_heap, (-1 * value, key))
        result = []
        while k > 0:
            result.append(heapq.heappop(max_heap)[1])
            k -= 1
        
        return result




        

        