class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurance = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if occurance != {} and rem in occurance:
                return [occurance[rem], i]
            occurance[nums[i]] = i