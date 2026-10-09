class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for item in nums:
            counter[item] = counter.get(item, 0) + 1
        
        counter_arr = []
        for key, v in counter.items():
            counter_arr.append((key, v))
        
        counter_arr = sorted(counter_arr, key=lambda x: x[1], reverse=True)
        result = [key for key, _ in counter_arr][:k]

        return result