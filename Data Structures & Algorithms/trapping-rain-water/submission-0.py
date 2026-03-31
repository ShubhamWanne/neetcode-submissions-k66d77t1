class Solution:
    def trap(self, height: List[int]) -> int:
        h_len = len(height)
        max_left = [0] * h_len
        max_right = [0] * h_len
        max_l = 0
        max_r = 0
        for i in range(h_len):
            max_left[i] = max_l
            max_l = max(height[i], max_l)
        #print(f"max_left: {max_left}")
        for i in range(h_len - 1, -1, -1):
            max_right[i] = max_r
            max_r = max(height[i], max_r)
        #print(f"max_right: {max_right}")        
        res = 0
        for i in range(h_len):
            temp_res = min(max_left[i], max_right[i]) - height[i]
            if temp_res > 0:
                res += temp_res
        return res