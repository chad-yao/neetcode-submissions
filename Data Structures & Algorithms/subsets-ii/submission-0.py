class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def backtrace(subset, nums, start):
            ans.append(deepcopy(subset))

            for i in range(start, len(nums)):
                # prune
                if i > start and nums[i] == nums[i-1]:
                    continue

                # choose this number
                subset.append(nums[i])
                backtrace(subset, nums, i + 1)

                # not choose
                subset.pop()

        backtrace([], nums, 0)

        return ans