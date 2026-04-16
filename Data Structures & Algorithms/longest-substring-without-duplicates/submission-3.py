class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0

        hset = set()
        max_len = 0

        while right < len(s):
            while s[right] in hset:
                hset.remove(s[left])
                left +=1 
            hset.add(s[right])
            max_len = max(right - left + 1, max_len)
            right += 1
            
        
        return max_len



        