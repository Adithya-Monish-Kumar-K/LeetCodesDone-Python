class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        g = defaultdict(list)
        id = [0] * numCourses
        for course, prereq in prerequisites:
            g[prereq].append(course)
            id[course] += 1
        q = deque([i for i in range(numCourses) if id[i] == 0])
        o = []
        while q:
            n = q.popleft()
            o.append(n)
            for i in g[n]:
                id[i] -= 1
                if id[i] == 0:
                    q.append(i)
        return o if len(o) == numCourses else []