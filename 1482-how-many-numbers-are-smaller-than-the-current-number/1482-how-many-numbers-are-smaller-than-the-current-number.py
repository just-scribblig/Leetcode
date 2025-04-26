class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        print(arr)
        # ans = [arr.index(i) for i in nums]
        ans = []
        for i in nums:
            ans.append(arr.index(i))
        return ans