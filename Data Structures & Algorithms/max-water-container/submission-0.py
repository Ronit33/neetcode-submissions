class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        max_volume = 0
        while i < j:
            volume = (j - i) * min(heights[i], heights[j])
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1

            max_volume = max(max_volume, volume)
        return max_volume

