class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 2
        ans = 0

        while r<n:
            if nums[l] + nums[r] == nums[l+1]/2:
                ans += 1
            l += 1
            r += 1
        return ans