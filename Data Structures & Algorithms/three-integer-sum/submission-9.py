class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4,-1,-1, 0, 1, 2
        sorted_nums = sorted(nums)
        res=[]
        for i in range(len(sorted_nums)):
            if i !=0 and sorted_nums[i] == sorted_nums[i-1]: continue
            first = sorted_nums[i]
            #print(f"first={first}")
            l, r = i+1, len(nums)-1
            while(l < r):
                #print(f"\t second={sorted_nums[l]} third={sorted_nums[r]}")
                t_sum = first + sorted_nums[l] + sorted_nums[r]
                if t_sum == 0:
                   res.append([first, sorted_nums[l], sorted_nums[r]])
                   r -=1
                elif t_sum < 0:
                    l +=1
                else:
                    r -=1

        res = list(set(tuple(row) for row in res))
        return res