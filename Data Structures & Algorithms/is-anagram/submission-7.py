class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Easy way -> sort the strings --> nlogn
        ## Efficient
        if len(s) != len(t):
            return False
        counterS, counterT = [0] * 26, [0] * 26
        for index in range(len(s)):
            counterS[ord(s[index]) - ord("a")] += 1
            counterT[ord(t[index]) - ord("a")] += 1
        return counterT == counterS



        