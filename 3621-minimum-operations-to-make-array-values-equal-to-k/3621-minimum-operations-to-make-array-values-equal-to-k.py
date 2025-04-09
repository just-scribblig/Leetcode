class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for i in nums:
            if i<k:
                return -1
        for i in set(nums):
            if i == k:
                return len(set(nums)) - 1
        return len(set(nums))