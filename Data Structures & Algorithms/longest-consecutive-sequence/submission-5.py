class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sorted_arr = sorted(nums)
        curr_count = 1
        max_count = 1
        i = 1
        print(sorted_arr)
        for i in range(len(nums)):
            if sorted_arr[i-1]+1 == sorted_arr[i]:
                curr_count += 1
                max_count = max(curr_count, max_count)
            elif sorted_arr[i-1]==sorted_arr[i]:
                pass
            else:
                curr_count = 1
        
        return max_count



        