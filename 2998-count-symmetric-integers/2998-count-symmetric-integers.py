class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high+1):
            digits = []
            while num > 0:
                digits.append(num%10)
                num //= 10
            n = len(digits)
            if n%2 != 0:
                continue
            mid = n//2
            first_half = sum(digits[:mid])
            second_half = sum(digits[mid:])
            if first_half == second_half:
                ans += 1
        return ans