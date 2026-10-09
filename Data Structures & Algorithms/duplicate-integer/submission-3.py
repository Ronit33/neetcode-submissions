class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for item in nums:
            if item not in tracker:
                tracker.add(item)
            else:
                return True
        
        return False