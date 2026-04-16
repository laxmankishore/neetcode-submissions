class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        index = 0
        while index < len(nums):
            temp = max(nums[index] + dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = temp
            index += 1
        return dp[1]
        



