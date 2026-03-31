class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #  arr= [   1,  2,  4,  6   ]
        #  pre= [   1,  2,  8,  48  ]
        #  suff=[   48, 48, 24, 6   ]
        #   ans=[   48, 24, 12, 8   ]
        pref = [1] * len(nums)
        postf = [1] * len(nums)
        prod = []
        for i in range(len(nums)):
            if i == 0:
                pref[i] = nums[i]
                continue
            pref[i] = pref[i-1] * nums[i]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1:
                postf[i] = nums[i]
                continue
            postf[i] = postf[i+1] * nums[i]
        for i in range(len(nums)):
            if i==0:
                prod.append(1*postf[i+1])
            elif i==len(nums)-1:
                prod.append(pref[i-1]*1)
            else:
                prod.append(pref[i-1]*postf[i+1])
        #print(f"Pref - {pref}")
        #print(f"Postf - {postf}")
        #print(f"Result - {prod}")
        return prod
        
        
            
        