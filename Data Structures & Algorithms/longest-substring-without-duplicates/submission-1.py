class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        h_set = set()

        left, right = 0, 0

        while right < len(s):
            while s[right] in h_set : 
                h_set.remove(s[left]) 
                    ## Iteration 4: hset = [z,x,y] 
                    ## s[right] is in hset  -> remove the duplicate in the hset 
                    ## Shrink the window left += 1
                left += 1
            h_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
            

        return max_length
            
            
        