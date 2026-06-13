class Solution:
    def twoSum(self, nums, target):
        num_dict = dict()
        for i in range(len(nums)):
            need = target - nums[i]


            if need in num_dict:
                return [num_dict[need], i]

            num_dict[nums[i]] = i