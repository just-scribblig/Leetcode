class Solution:
    def countBits(self, n: int) -> List[int]:
        def bin(k):
            l=0
            while True:
                l=l+(k%2)
                if k/2<1:
                    break
                k=k//2
            return l
        k=[bin(i) for i in range(n+1)]
        return k