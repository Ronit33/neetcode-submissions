class Solution:
    def get_triplets(self, nums, idx):
        n = len(nums)
        target = 0
        l = idx + 1
        r = n - 1
        triplets = []
        while l < r:
          
            sm = nums[l] + nums[r] + nums[idx]
            if sm == target:
                triplets.append([nums[idx], nums[l], nums[r]])

                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif sm < target:
              l += 1
            else:
              r -= 1
              

              
        
        return triplets
            

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        i = 0
        result = []
        while i < n:
            if sorted_nums[i] > 0:
                break
            triplets = self.get_triplets(sorted_nums, i)
            result.extend(triplets)
          
            while i < n-1 and sorted_nums[i] == sorted_nums[i+1]:
                i += 1
            i += 1
        
        return result