class Solution:
    def combinationSum2(self, candidates, target):

        candidates.sort()

        res = []
        subset = []

        def backtrack(start, remain):

            if remain == 0:
                res.append(subset[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                subset.append(candidates[i])

                backtrack(i + 1, remain - candidates[i])

                subset.pop()

        backtrack(0, target)

        return res