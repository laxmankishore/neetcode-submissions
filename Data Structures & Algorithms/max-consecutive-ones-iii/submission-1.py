class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_width = 0
        num_zeroes = 0
        left = 0
        for right in range(len(nums)):

            ## checking for condition to compress the window
            if nums[right] == 0:
                num_zeroes += 1
                while num_zeroes > k:
                    if nums[left] == 0:
                        num_zeroes -= 1
                    left += 1

            w_len = right - left + 1
            max_width = max(w_len, max_width)
        
        return max_width


                


        

        