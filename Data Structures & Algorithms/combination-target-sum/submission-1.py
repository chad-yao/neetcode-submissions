class Solution:
    def combinationSum(self, nums, target):
        ans = []

        def backtrace(subset, nums, k, start):
            if k == 0:
                ans.append(deepcopy(subset))
                return
            if k < 0:
                return

            for i in range(start, len(nums)):
                # if pick the number
                subset.append(nums[i])
                backtrace(subset, nums, k-nums[i], i)

                # if not pick the number
                subset.pop()

        backtrace([],nums,target,0)
        return ans