class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for item in nums:
            counter[item] = counter.get(item, 0) + 1
        
        result = sorted(counter, key=counter.get, reverse=True)[:k]

        return result