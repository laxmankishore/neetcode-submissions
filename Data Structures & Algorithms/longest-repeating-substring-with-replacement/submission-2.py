class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        hmap = {}
        result = 0
        left = 0

        max_count = 0

        for right in range(len(s)):
            hmap[s[right]] = 1 + hmap.get(s[right], 0)
            max_count = max(max_count, hmap[s[right]])

            while right - left + 1 - max_count > k:
                hmap[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        
        return result



        