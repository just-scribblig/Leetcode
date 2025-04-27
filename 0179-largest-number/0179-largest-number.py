class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            nums[i] = str(nums[i])
        
        def compare(n1,n2):
            if n1+n2 > n2+n1:
                return -1
            if n1+n2 < n2+n1:
                return 1
            else:
                return 0
        ans = "".join(sorted(nums, key=cmp_to_key(compare)))

        return ans if int(ans)!=0 else "0"