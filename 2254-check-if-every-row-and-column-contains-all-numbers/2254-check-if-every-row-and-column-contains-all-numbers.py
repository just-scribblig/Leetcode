class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected = set(range(1,n+1))
        for i in range(1,n):
            if set(matrix[i]) != expected:
                return False

        for i in range(n):
            col_set = set()
            for j in range(n):
                col_set.add(matrix[j][i])
            if col_set != expected:
                return False

        return True