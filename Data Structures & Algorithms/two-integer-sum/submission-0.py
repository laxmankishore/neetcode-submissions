class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index in range(len(nums)): 
            diff = target - nums[index]
            if diff in hmap:
                return [hmap[diff], index]
            else :
                hmap[nums[index]] = index
        return []


        