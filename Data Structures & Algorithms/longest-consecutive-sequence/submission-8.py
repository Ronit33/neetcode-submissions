class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0
        for item in num_set:
            if item-1 not in num_set:
                count = 1
                while item + count in num_set:
                    count += 1
            
                max_count = max(max_count, count)            
        return max_count