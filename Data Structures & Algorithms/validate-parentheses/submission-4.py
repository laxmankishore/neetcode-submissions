class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        hmap = {")": "(", "}": "{", "]":"["}
        stack = []
        index = 0
        while index < len(s):
            if s[index] in hmap:
                if stack and hmap[s[index]] == stack[-1]:
                    stack.pop()
                else :
                    return False
            else:
                stack.append(s[index])
            index +=1
    

        return not stack
        