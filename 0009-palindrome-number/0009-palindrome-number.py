class Solution:
    def isPalindrome(self, x: int) -> bool:
        if '-' in str(x):
            return False
        x = str(x)
        l = 0
        r = len(x)-1
        while l<r:
            if x[r] != x[l]:
                return False
            r -= 1
            l += 1
        return True