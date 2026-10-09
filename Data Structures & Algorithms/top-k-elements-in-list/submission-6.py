class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        max_count = 0
        for item in nums:
            counter[item] = counter.get(item, 0) + 1
            max_count = max(max_count, counter[item])
        
        buckets = [[] for _ in range(max_count+1)]

        for n, count in counter.items():
            buckets[count].append(n)
        
        res = []

        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
            
            if len(res)==k:
                return res


        

