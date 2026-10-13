class Solution:
    def triplet_sum(self, rem_nums, target):
        n = len(rem_nums)
        i = 0
        j = n - 1
        sum_results = []
        while i < j:
            sm = rem_nums[i] + rem_nums[j]
            if sm == target:
                sum_results.append([-target, rem_nums[i], rem_nums[j]])
                i+=1
                j-=1
            elif sm < target:
                i += 1
            else:
                j -= 1
        return sum_results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = list(sorted(nums))
        results = set()
        n = len(sorted_nums)
        for i in range(n):
            triplets = self.triplet_sum(sorted_nums[i+1:], -sorted_nums[i])
            for trp in triplets:
                results.add(tuple(trp))

        return list(results)



        