class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)

        ans = []

        def backtrace(subset, nums, used):
            if len(subset) == len(nums):
                ans.append(deepcopy(subset))
                return

            for i in range(len(nums)):
                # if already being chosen
                if used[i]:
                    continue

                # choose the number
                used[i] = True
                subset.append(nums[i])
                backtrace(subset, nums, used)

                # not choose
                used[i] = False
                subset.pop()
        backtrace([],nums,used)
        return ans