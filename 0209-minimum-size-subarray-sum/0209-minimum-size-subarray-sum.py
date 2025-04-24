class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        s = 0
        ans = math.inf
        for r in range(n):
            s += nums[r]
            while s >= target:
                ans = min(ans, r-l+1)
                s -= nums[l]
                l += 1 
        return 0 if ans > n else ans
