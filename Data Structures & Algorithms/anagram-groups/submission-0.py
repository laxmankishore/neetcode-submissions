class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for index in range(len(strs)):
            count = [0] * 26
            for c in strs[index]:
                count[ord(c) - ord('a')] += 1
            answer[tuple(count)].append(strs[index])
        return list(answer.values())