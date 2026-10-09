class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join("<sep>" + s for s in strs)


    def decode(self, s: str) -> List[str]:
        return s.split("<sep>")[1:]