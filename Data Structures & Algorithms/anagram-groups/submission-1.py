class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_hash = {}
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            
            key = tuple(counts)
            if key not in anagram_hash:
                anagram_hash[key] = []
            anagram_hash[key].append(s)

        
        return list(anagram_hash.values())