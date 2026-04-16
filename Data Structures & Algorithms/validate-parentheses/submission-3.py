class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
           "]": "[",
           "}": "{",
           ")": "(" 
        }
        stk = []
        for char in s:
            if char not in hmap:
                stk.append(char)
            else:
                if not stk:
                    return False
                elif stk.pop() != hmap[char]:
                    return False
        
        return True if not stk else False
            
        