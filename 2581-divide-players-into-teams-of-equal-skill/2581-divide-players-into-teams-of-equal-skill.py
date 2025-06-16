class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)

        res = []
        l, r = 0, len(skill)-1
        while l<r:
            res.append([skill[l], skill[r]])
            l += 1
            r -= 1
        
        for i in range(n//2 - 1):
            if sum(res[i]) != sum(res[i+1]):
                return -1
        ans = 0
        for (first, second) in res:
            ans += first*second
        return ans
