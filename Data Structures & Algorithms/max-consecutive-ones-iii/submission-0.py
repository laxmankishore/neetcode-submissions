class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0
        max_width = float("-inf")
        
        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                while zero_count > k:
                    if nums[left] == 0:
                        zero_count -= 1
                    left += 1

            width = right - left + 1
            max_width = max(max_width, width)
            right += 1
        
        return max_width

                
            






        