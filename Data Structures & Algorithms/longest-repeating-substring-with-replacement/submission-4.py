class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_width = 0
        left = 0
        freq_counter = {}
        for right in range(len(s)):
            freq_counter[s[right]] = 1 + freq_counter.get(s[right], 0)
            while (right - left + 1) - max(freq_counter.values()) > k:
                freq_counter[s[left]] -= 1
                left += 1
            max_width = max(right - left + 1, max_width)
        return max_width        