class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(r, c, s):
            if r == 0:
                result.append(list(c))
                return
            elif r < 0:
                return
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue
                c.append(candidates[i])
                backtrack(r - candidates[i], c, i + 1)
                c.pop()
        backtrack(target, [], 0)
        return result