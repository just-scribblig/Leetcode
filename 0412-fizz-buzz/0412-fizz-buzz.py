class Solution:
    def value(self, n):
        if n%5 == n%3 == 0:
            return "FizzBuzz"
        elif n%3 == 0:
            return "Fizz"
        elif n%5 == 0:
            return "Buzz"
        return f"{n}"
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            res.append(self.value(i))
        return res