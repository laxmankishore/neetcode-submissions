class Solution:
    def getCounterKey(self, string: str):
        counter = [0] * 26
        for char in string:
            counter[ord(char) - ord("a")] += 1
        return counter

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {} ## Ex:{key("ana1"): [ana1, aan1]} etc.., 
        for string in strs:
            key = tuple(self.getCounterKey(string))
            if key in hmap:
                hmap[key].append(string)
            else:
                hmap[key] = [string]
            
        return list(hmap.values())





        