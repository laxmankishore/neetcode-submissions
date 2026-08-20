class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        # or simply just use return nums*2
#Python's * operator duplicates list memory references instantly.When you run nums * 2, Python executes an optimized internal C function (list_repeat) under the hood instead of running standard Python loops.CPython Internal StepsCalculates size: Multiplies current length by two.Allocates memory: Reserves a new contiguous block.Copies pointers: Copies object references sequentially.Repeats sequence: Appends the exact same pointers again.
        
        