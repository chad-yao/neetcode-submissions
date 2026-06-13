class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def backtracing(start):
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtracing(i+1)
                subset.pop()

        backtracing(0)
        return res