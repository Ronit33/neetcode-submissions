class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        longest = 0
        l = 0

        for r in range(n):
            if s[r] not in seen:
                seen[s[r]] = r
            else:
                if l <= seen[s[r]]:
                    l = seen[s[r]] + 1
                seen[s[r]] = r

            longest = max(longest, r - l + 1)

        
        return longest

