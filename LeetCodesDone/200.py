class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rs, cs = len(grid), len(grid[0])
        v = set()
        islands = 0
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rs or c >= cs or
                grid[r][c] == '0' or
                (r, c) in v
            ):
                return
            v.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(rs):
            for c in range(cs):
                if grid[r][c] == '1' and (r, c) not in v:
                    dfs(r, c)
                    islands += 1
        return islands