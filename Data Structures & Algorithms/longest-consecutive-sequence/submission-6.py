class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        num_set = set(nums)
        starts = []
        max_count = 1
        for item in num_set:
            if item-1 not in num_set:
                count = 1
                while item + count in num_set:
                    count += 1
            
                max_count = max(max_count, count)            
        return max_count