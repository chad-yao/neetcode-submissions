class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        N = len(temperatures)
        ans = [0 for _ in range(N)]
        
        for i in range(N):
            if len(stack) == 0:
                stack.append((i, temperatures[i]))
                continue

            while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                idx, temp = stack.pop()

                ans[idx] = i - idx
            
            stack.append((i, temperatures[i]))

        return ans

            


            