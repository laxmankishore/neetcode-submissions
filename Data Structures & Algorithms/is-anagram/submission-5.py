class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = [0] * 26
        counterT = [0] * 26

        for index in range(len(s)):
            counterS[ord(s[index]) - ord("a")] += 1
        for index in range(len(t)):
            counterT[ord(t[index]) - ord("a")] += 1
        
        return counterS == counterT

        

        
        
        