class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        longest = 0
        l = 0

        for r in range(n):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            
            seen[s[r]] = r

            longest = max(longest, r - l + 1)

        
        return longest

