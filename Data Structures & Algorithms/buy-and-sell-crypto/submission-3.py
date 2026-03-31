class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        s = 0
        res = 0
        for i in range(len(prices)):
            if i == 0:
                b = prices[i]
            else:
                if prices[i] < b:
                    b = prices[i]
                else:
                    s = prices[i]
            print(f"current_price: {prices[i]} b: {b} s: {s}")
            t_res = s - b
            if t_res >= 0:
                res = max(res, t_res)
                s = 0
        return res 