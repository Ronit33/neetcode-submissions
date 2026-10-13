class Solution:
    def triplet_sum(self, nums, start_idx, target):
        n = len(nums)
        i = 0
        j = n - 1
        sum_results = []
        while i < j:
            if i > start_idx:
                sm = nums[i] + nums[j]
                if sm == target:
                    sum_results.append([-target, nums[i], nums[j]])
                    i+=1
                    j-=1
                elif sm < target:
                    i += 1
                else:
                    j -= 1
            else:
                i += 1
        return sum_results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = list(sorted(nums))
        results = set()
        n = len(sorted_nums)
        for i in range(n):
            if sorted_nums[i]>0:
                break
            triplets = self.triplet_sum(sorted_nums, i, -sorted_nums[i])
            for trp in triplets:
                results.add(tuple(trp))

        return list(results)



        