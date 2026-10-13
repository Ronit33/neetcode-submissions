class Solution:
    def triplet_sum(self, nums, start_idx, target):
        n = len(nums)
        i = start_idx + 1
        j = n - 1
        sum_results = []
        while i < j:
            sm = nums[i] + nums[j]
            if sm == target:
                sum_results.append([-target, nums[i], nums[j]])
                while i < j and nums[i]==nums[i+1]:
                    i+=1
                while i < j and nums[j-1]==nums[j]:
                    j-=1
                i+=1
                j-=1
            elif sm < target:
                i+=1
            else:
                j -= 1

        return sum_results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = list(sorted(nums))
        results = []
        n = len(sorted_nums)
        i = 0
        while i < n:
            if sorted_nums[i]>0:
                break
            triplets = self.triplet_sum(sorted_nums, i, -sorted_nums[i])
            while i+1 < n and sorted_nums[i]==sorted_nums[i+1]:
                i+=1
            
            results.extend(triplets)

            i+=1

        return results



        