class Solution:
    def isPrime(self, n: int) -> bool:
        if n<2:
            return False
        for i in range(2, int(n**0.5+1)):
            if n%i == 0:
                return False
        return True
    def checkPerfectNumber(self, num: int) -> bool:
        for i in range(2, 18):
            if self.isPrime(i) and self.isPrime(2**(i)-1):
                if 2**(i-1)*(2**(i)-1) == num:
                    return True
        return False

