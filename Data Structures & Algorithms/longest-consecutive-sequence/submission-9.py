class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        starts = []
        for item in uniques:
            if item-1  not in uniques:
                starts.append(item)

        max_count = 0
        for st in starts:
            count = 1
            while st + count in uniques:
                count += 1
            max_count = max(max_count, count)

        return max_count
