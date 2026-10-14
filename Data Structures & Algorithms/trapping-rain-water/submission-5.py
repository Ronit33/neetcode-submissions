class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n-1
        left_max = height[0]
        right_max = height[-1]
        total_water = 0

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                curr_water = left_max - height[l]
                l += 1
            else:
                curr_water = right_max - height[r]
                r -= 1
            total_water += curr_water
        
        return total_water
            