class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for val in nums:
            if val-1 not in nums:
                seq_count = 0
                while val+seq_count in nums:
                    seq_count += 1
                longest = max(longest, seq_count)
        return longest
