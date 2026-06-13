class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = dict()

        for i in range(len(nums)):
            num_dict[nums[i]] = 1 + num_dict.get(nums[i], 0)

            if num_dict[nums[i]] > 1:
                return True
        
        return False