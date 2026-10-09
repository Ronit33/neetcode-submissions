class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}
        for s in strs:
            encoded = [0] * 26
            for char in s:
                encoded[ord(char) - ord('a')] += 1
            key = tuple(encoded)

            if key not in anagram_hash:
                anagram_hash[key] = [s]
            else:
                anagram_hash[key].append(s)
        
        return list(anagram_hash.values())