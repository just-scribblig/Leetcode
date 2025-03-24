class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        k=""
        for i in t:
            if i not in s:
                k=i
            else:
                s=s.replace(i,"",1)
        return k