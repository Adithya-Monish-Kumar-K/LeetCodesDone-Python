class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs = [set() for _ in range(9)]
        cs = [set() for _ in range(9)]
        bs = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.':
                    continue
                bi = (r // 3) * 3 + (c // 3)
                if (n in rs[r]) or (n in cs[c]) or (n in bs[bi]):
                    return False
                rs[r].add(n)
                cs[c].add(n)
                bs[bi].add(n)
        return True