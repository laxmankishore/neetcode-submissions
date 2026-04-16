class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if nums[index] in hmap:
                return [hmap[nums[index]], index]
            hmap[diff] = index
        return []




        