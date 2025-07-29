class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for i in range(max(0, r - 1), min(m, r + 2)):
                    for j in range(max(0, c - 1), min(n, c + 2)):
                        if i == r and j == c:
                            continue
                        if board[i][j] == 1 or board[i][j] == 2:
                            live_neighbors += 1

                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 2
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 3

        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
