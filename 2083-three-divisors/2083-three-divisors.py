class Solution:
    def isThree(self, n: int) -> bool:
        def isPrime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i == 0:
                    return False
            return True
        root = sqrt(n)
        if root == int(root):
            if isPrime(root):
                return True
        return False