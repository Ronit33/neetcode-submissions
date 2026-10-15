class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 1
        if s=="":
            return 0
        # for i in range(n):
        #     ss_set = set([s[i]])
        #     curr_count = 1
        #     for j in range(i+1, n):
        #         if s[j] in ss_set:
        #             break
        #         curr_count += 1
        #         ss_set.add(s[j])
        #     longest = max(longest, curr_count)

        l = 0
        ss_set = set(s[l])
        curr_count = 1
        for r in range(l+1, n):

            if s[r] not in ss_set:
                ss_set.add(s[r])
            else:
                while s[l] != s[r]:
                    ss_set.remove(s[l])
                    l += 1
                l += 1
                
            longest = max(longest, len(ss_set))


        
        return longest
