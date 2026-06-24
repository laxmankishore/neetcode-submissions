class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for index in range(len(nums)):
            if nums[index] in hset:
                return True
            hset.add(nums[index])
        return False