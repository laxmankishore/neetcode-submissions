class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for index in range(len(nums)):
            if nums[index] in hmap:
                return [hmap[nums[index]], index]
            else:
                diff = target - nums[index]
                hmap[diff] = index


        