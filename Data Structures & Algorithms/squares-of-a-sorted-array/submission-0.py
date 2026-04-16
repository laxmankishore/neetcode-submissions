class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        index = length - 1

        left, right = 0, length - 1

        while left <= right :
            if abs(nums[left]) <= abs(nums[right]):
                result[index] = nums[right] * nums[right]
                right -= 1
            else :
                result[index] = nums[left] * nums[left]
                left += 1
            index -= 1
        
        return result
            

        