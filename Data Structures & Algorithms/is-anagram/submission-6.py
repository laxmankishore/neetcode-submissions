class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = [0]*26
        counterT = [0]*26

        for char in s:
            counterS[ord(char) - ord("a")] += 1
        for char in t :
            counterT[ord(char) - ord("a")] += 1
        
        return counterT == counterS
        

        
        
        