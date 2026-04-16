class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res+= ","
        
        res += "#"
        # for s in strs:
        #     res += s
        
        return res + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s :
            return []

        sizes, res, index = [], [], 0
        while s[index] != "#":
            cur = ""
            while s[index] != ',':
                cur += s[index]
                index += 1
            sizes.append(int(cur))
            index += 1
        index += 1
        for sz in sizes :
            res.append(s[index: index + sz])
            index += sz
        return res


