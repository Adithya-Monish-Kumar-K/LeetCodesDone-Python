class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(r, c, s):
            if r == 0:
                result.append(list(c))
                return
            elif r < 0:
                return

            for i in range(s, len(candidates)):
                c.append(candidates[i])
                backtrack(r - candidates[i], c, i)
                c.pop()

        backtrack(target, [], 0)
        return result