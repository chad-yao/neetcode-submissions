class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0

        N = len(s)

        if N == 0:
            return 0

        ans = 0
        maxf = 0
        count = {}
        while r < N:
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            ans = max(ans, r - l + 1)
            r += 1
            
            

        return ans

