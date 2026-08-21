class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ## Expand the window on every iteration  - check for length
        ## -> compress on a condition
        ## cond -> if a duplicate is identified - will use set to track
        ## -> compress till left reaches the duplicated value and remove left elements 
        ## from set

        max_len = 0
        hset = set()
        left = 0

        for right in range(len(s)):
            if s[right] in hset:
                while s[right] in hset:
                    hset.remove(s[left])
                    left += 1
            w_len = right - left + 1
            max_len = max(w_len, max_len)
            hset.add(s[right])
        
        return max_len

        