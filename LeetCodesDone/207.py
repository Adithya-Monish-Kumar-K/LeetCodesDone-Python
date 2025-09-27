class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        g = defaultdict(list)
        d = [0] * numCourses
        for c, p in prerequisites:
            g[p].append(c)
            d[c] += 1
        q = deque([i for i in range(numCourses) if d[i] == 0])
        cc = 0
        while q:
            c = q.popleft()
            cc += 1
            for n in g[c]:
                d[n] -= 1
                if d[n] == 0:
                    q.append(n)
        return cc == numCourses