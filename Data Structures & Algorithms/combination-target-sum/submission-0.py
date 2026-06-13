class Solution:
    def combinationSum(self, nums, target):
        res = []
        subset = []

        def backtrack(start, remain):
            if remain == 0:
                res.append(subset[:])
                return

            if remain < 0:
                return

            for i in range(start, len(nums)):
                subset.append(nums[i])

                # i, not i + 1
                # because same number can be reused
                backtrack(i, remain - nums[i])

                subset.pop()

        backtrack(0, target)
        return res