class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # left = 0
        # curr_sum = sum(nums[:k])
        # max_sum = curr_sum
        # for right in range(k, len(nums)):
        #     curr_sum += nums[right] - nums[left]
        #     max_sum = max(curr_sum, max_sum)
        #     left += 1
        
        # return round(float(max_sum)//k, 5)

        right = 0
        max_sum = float("-inf")
        curr_sum = 0

        while right < len(nums):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)
            right += 1
        
        return max_sum








        