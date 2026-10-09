class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for i in range(len(nums)):
            if nums[i] in checker:
                return [checker[nums[i]], i]
            rem = target - nums[i]
            checker[rem] = i
            