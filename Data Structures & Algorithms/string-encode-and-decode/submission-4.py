class Solution:

    def encode(self, strs: List[str]) -> str:
        ## Basic can use a special char to seperate
        ## But constraint has all 256 chars
        ## Use len and followed by str -> len + "place holder for string"
        result = ""
        for string in strs:
            result = result + str(len(string)) + "#" + string
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        while index < len(s):
            dim_index = s.find("#", index)
            length = int(s[index:dim_index])
            start = dim_index + 1
            end = start + length
            result.append(s[start : end])
            index = end
        return result


