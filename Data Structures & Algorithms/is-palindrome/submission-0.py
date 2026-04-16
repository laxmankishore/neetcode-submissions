import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = re.findall(r"[a-zA-Z0-9]+", s.lower())
        s = "".join(s_list)
        left, right = 0, len(s) - 1
        
        while left < right :
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        