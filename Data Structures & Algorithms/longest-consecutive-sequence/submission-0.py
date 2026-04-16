class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numSet = set(nums)
        long_streak = 0

        for num in numSet:
            if (num - 1) not in numSet:
                current_num = num
                current_streak = 1

                while (current_num + 1) in numSet:
                    current_num += 1
                    current_streak += 1

                long_streak = max(long_streak, current_streak)
        return long_streak


        