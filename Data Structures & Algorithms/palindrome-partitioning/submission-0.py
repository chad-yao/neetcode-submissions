class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        k = len(s)

        def is_palindrome(string: str) -> bool:
            l, r = 0, len(string) - 1

            while l < r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(subset, substr):
            if len(substr) == 0:
                ans.append(deepcopy(subset))

            for i in range(1, len(substr) + 1):
                temp_1 = substr[0:i]
                temp_2 = substr[i:]

                if not is_palindrome(temp_1):
                    continue
                
                subset.append(temp_1)
                backtrack(subset, temp_2)
                subset.pop()
        
        backtrack([], s)

        return ans
