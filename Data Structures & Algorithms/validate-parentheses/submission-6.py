class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        hmap = {"}":"{", ")":"(", "]":"["}

        stack = []
        for char in s:
            if char in hmap:
                if stack and stack[-1] == hmap[char]:
                    stack.pop()
                else :
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False




        

        