class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        
        rs, cs = len(matrix), len(matrix[0])
        frz = any(matrix[0][j] == 0 for j in range(cs))
        fcz = any(matrix[i][0] == 0 for i in range(rs))

        for i in range(1, rs):
            for j in range(1, cs):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rs):
            if matrix[i][0] == 0:
                for j in range(1, cs):
                    matrix[i][j] = 0

        for j in range(1, cs):
            if matrix[0][j] == 0:
                for i in range(1, rs):
                    matrix[i][j] = 0

        if frz:
            for j in range(cs):
                matrix[0][j] = 0

        if fcz:
            for i in range(rs):
                matrix[i][0] = 0