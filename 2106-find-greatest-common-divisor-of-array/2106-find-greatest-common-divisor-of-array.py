class Solution:
    def findGCD(self, nums: List[int]) -> int:
        M = max(nums)
        m = min(nums)
        set1 = {1}
        for i in range(2,m+1):
            if m%i == 0:
                set1.add(i)
        set2 = {1}
        for i in range(2,M+1):
            if M%i == 0:
                set2.add(i)
        return max(set1.intersection(set2))