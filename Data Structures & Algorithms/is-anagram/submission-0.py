class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmapS, hmapT = {},{}
        for index in range(len(s)):
            hmapS[s[index]] = 1 + hmapS.get(s[index], 0)
            hmapT[t[index]] = 1 + hmapT.get(t[index], 0)
        return hmapS == hmapT

        
        
        