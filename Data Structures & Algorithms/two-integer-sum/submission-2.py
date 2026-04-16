class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## For Sorted Order

        # left = 0
        # right = len(nums) - 1

        # while left < right :
        #     val = nums[left] + nums[right]
        #     if val == target:
        #         return [left, right]
        #     elif target > val :
        #         left += 1
        #     else :
        #         right -= 1
        
        # return []

        ## Not in sorted Order

        hmap = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if nums[index] in hmap:
                return [hmap[nums[index]], index]
            hmap[diff] = index
        
        return []


        