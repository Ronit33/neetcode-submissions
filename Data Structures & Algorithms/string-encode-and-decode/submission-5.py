class Solution:

    def encode(self, strs: List[str]) -> str:

        return "".join([f"{len(s)}#{s}" for s in strs])

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            string_len = int(s[i: j])
            string_found = s[j+1: string_len + j + 1]
            result.append(string_found)
            i = string_len + j + 1


        return result
