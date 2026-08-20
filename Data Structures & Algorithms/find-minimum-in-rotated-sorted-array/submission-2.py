class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        ## Trying to find out min ex: [4, 5, 6, l - 7, 8, mid -> 1, 2, r - 3] -
        # l = 2 -> val 6
        # r = 4 -> val 3 -> mid_index = 3

        # Another example - [7, 1, 2, 3, 4, 5, 6]
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else : 
                right = mid 
        return nums[left]









        