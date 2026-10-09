class Solution:

    def encode(self, strs):
        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s):
        result, i = [], 0
        while i < len(s):
            for j in range(i, len(s)):
                if s[j]=="#":
                    break
            len_s = int(s[i:j])
            result.append(s[j + 1: j + 1 + len_s])
            i = j + 1 + len_s
        
        return result