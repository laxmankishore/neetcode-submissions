class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = {}
        for char in ransomNote:
            if char in hmap :
                hmap[char] += 1
            else:
                hmap[char] = 1
        
        for char in magazine:
            if char in hmap:
                if hmap[char] > 1:
                    hmap[char] -= 1
                else :
                    del hmap[char]
        
        return True if len(hmap) == 0 else False
        