class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0

        N = len(s)

        if N == 0:
            return 0
        ans = 0
        while r < N:
            substr = s[l:r+1]
            str_set = set(substr)

            if len(substr) == len(str_set):
                ans = max(ans, len(substr))
                r+=1
            else:
                l+=1

        return ans

        