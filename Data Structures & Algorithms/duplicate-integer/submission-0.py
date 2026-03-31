class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates =  {}
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates[nums[i]] = 1
            else:
             duplicates[nums[i]] = duplicates[nums[i]] + 1
        for i in duplicates.values():
            if i > 1: return True
        return False


