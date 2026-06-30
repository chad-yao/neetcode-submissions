class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtracking(substring, openN, closeN):
            if openN == closeN == n:
                ans.append(deepcopy(substring))
                return
            
            # add (
            if openN < n:
                substring += "("
                backtracking(substring, openN + 1, closeN)
                substring = substring[:-1]

            # add )
            if closeN < openN:
                substring += ")"
                backtracking(substring, openN, closeN + 1)
                substring = substring[:-1]

        backtracking("",0,0)

        return ans

            
