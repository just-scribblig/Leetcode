class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        if m==0 or n==0:
            return 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] < 0:
                    count += 1
        return count