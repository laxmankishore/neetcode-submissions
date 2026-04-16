class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)
        hset = set()
        left = 0
        max_width = 0
        for right in range(length):
            curr_char = s[right]
            while curr_char in hset:
                hset.remove(s[left])
                left += 1
            hset.add(curr_char)
            width = right - left + 1
            max_width = max(width, max_width)
        
        return max_width


            


    

        