class Solution:
    def twoSum(self, nums, target):
        x_tuple = []

        for i in range(len(nums)):
            x_tuple.append((nums[i], i))

        x_tuple.sort(key=lambda x: x[0])

        left = 0
        right = len(nums) - 1

        while left < right:
            two_sum = x_tuple[left][0] + x_tuple[right][0]

            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                break
        a, b = x_tuple[left][1], x_tuple[right][1]
        if a < b:
            return [a, b]
        else:
            return [b, a]