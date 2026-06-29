class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)

        def backtracking(perms, nums, used):
            if len(perms) == len(nums):
                ans.append(perms[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                perms.append(nums[i])
                used[i] = True

                backtracking(perms, nums, used)

                perms.pop()
                used[i] = False
        backtracking([], nums, used)

        return ans
            