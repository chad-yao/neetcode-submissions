class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = dict()


        for i in range(len(nums)):
            table[nums[i]] = 1 + table.get(nums[i], 0)

        best_ans = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in table.keys():
                k = 1
                while nums[i] + k in table.keys():
                    k += 1
                if k >= best_ans:
                    best_ans = k
        return best_ans