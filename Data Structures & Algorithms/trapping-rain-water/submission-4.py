class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n<=0:
            return 0
        full_water = 0
        running_left_max = [height[0] for _ in range(n)]
        running_right_max = [height[-1] for _ in range(n)]

        for i in range(1, n):
            running_left_max[i] = max(height[i], running_left_max[i-1])

        for i in range(n-2, -1, -1):
            running_right_max[i] = max(height[i], running_right_max[i+1])
            
        
        for i in range(1, n-1):
            m_lh = running_left_max[i]
            m_rh = running_right_max[i]
            curr_water = min(m_lh, m_rh) - height[i]
            full_water += curr_water
        return full_water