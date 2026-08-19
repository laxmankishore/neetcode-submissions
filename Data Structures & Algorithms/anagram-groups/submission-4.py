class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord("a")] += 1
            key = tuple(counter)
            if key in hmap:
                hmap[key].append(word)
            else :
                hmap[key] = [word]
        
        return list(hmap.values())

        