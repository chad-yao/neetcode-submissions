class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = [-num for num in nums]
        heapq.heapify(new_nums)

        for i in range(k):
            ans = -heapq.heappop(new_nums)

        return ans