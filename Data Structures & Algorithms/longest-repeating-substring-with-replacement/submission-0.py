class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # char_set = set(s)
        # # if len(char_set) >= len(s) - 2:
        # #     return len(s)

        # max_length = 0
    
        # for c in char_set :
        #     count = left = 0
        #     for right in range(len(s)):
        #         if s[right] == c:
        #             count += 1

        #         while (right - left + 1) - count > k:
        #             if s[left] == c:
        #                 count -= 1
        #             left += 1
        #         max_length = max(max_length, right - left + 1)
        
        # return max_length
                
        hmap = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            hmap[s[right]] = 1 + hmap.get(s[right], 0)
            while (right - left + 1) - max(hmap.values()) > k:
                hmap[s[left]]  -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length



                



        