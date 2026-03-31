class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurance = {}
        for i in range(len(nums)):
            if nums[i] in occurance:
                occurance[nums[i]] += 1
            else:
                occurance[nums[i]] = 1
        reverse_sorted_d = dict(sorted(occurance.items(), key= lambda x: x[1], reverse=True))
        return list(reverse_sorted_d.keys())[:k]
            