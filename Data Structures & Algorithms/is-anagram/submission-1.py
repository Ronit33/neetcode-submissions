class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vocab = "qwertyuiopasdfghjklzxcvbnm"

        for char in vocab:
            if s.count(char) != t.count(char):
                return False

        return True