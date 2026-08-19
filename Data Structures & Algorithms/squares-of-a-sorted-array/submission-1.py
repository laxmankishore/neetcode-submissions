class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        curr_index = len(nums) - 1

        while left <= right:
            left_val = nums[left]*nums[left]
            right_val = nums[right]*nums[right]
            if left_val > right_val:
                result[curr_index] = left_val
                left += 1
            else:
                result[curr_index] = right_val
                right -= 1
            curr_index -= 1
        
        return result



        