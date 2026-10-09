class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram_hash = defaultdict(list)

        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) - ord('a')] += 1
            
            key = tuple(counts)

            anagram_hash[key].append(s)
        
        return list(anagram_hash.values())