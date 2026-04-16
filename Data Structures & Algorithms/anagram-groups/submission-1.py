class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list)
        for word in strs:
            counter = [0] * 26

            for char in word:
                counter[ord(char) - ord("a")] += 1
            hmap[tuple(counter)].append(word)
        
        return list(hmap.values())

        