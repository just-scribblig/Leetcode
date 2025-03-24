class Solution:
    def convertToBase7(self, num: int) -> str:
        n=num
        i=1
        k=""
        if num<0:
            k="-"
            n=-1*n
        while i*7<=n:
            i=i*7
        while i>0:
            k=k+str(n//i)
            n=n%i
            i=i//7
        return k