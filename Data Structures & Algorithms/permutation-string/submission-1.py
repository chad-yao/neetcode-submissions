class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0

        K = len(s1)
        N = len(s2)

        if K > N:
            return False

        count = Counter(s1)
        while r < N:
            count[s2[r]] = count.get(s2[r], 0) - 1

            while count[s2[r]] < 0:
                count[s2[l]] += 1
                l += 1

            if r - l + 1 == K:
                return True

            r += 1
            
        return False