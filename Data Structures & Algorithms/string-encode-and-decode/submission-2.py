class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs :
            return ""
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        if not s :
            return []

        index = 0
        res = []
        while index < len(s):
            j = index
            while s[j] != "#":
                j += 1
            length = int(s[index:j])
            index = j + 1
            j = index + length
            res.append(s[index:j])
            index = j
        return res

