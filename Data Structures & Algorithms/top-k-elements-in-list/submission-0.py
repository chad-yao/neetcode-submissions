class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []

        x_dict = dict()

        for i in range(len(nums)):
            x_dict[nums[i]] = 1 + x_dict.get(nums[i], 0)
        

        for key, value in x_dict.items():
            heapq.heappush(heap, (-value, key))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans