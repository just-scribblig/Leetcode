class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            for j in range(n):
                ans += mat[i][j] if i==j else mat[i][j] if i+j==n-1 else 0
        return ans