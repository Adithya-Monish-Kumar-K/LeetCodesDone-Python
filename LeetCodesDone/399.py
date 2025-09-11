class Solution:
    def calcEquation(self, equations: List[List[str]], vs: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        g = defaultdict(list)
        for (a, b), v in zip(equations, vs):
            g[a].append((b, v))
            g[b].append((a, 1 / v))
        def dfs(src, dst, visited):
            if src not in g or dst not in g:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for n, v in g[src]:
                if n not in visited:
                    p = dfs(n, dst, visited)
                    if p != -1.0:
                        return p * v
            visited.remove(src)
            return -1.0
        r = []
        for src, dst in queries:
            r.append(dfs(src, dst, set()))
        return r