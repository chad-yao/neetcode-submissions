class Solution:
    def isValid(self, s: str) -> bool:
        left = ["[","{","("]
        right = ["]","}",")"]

        if len(s) == 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top_left = stack.pop()
                idx_left = left.index(top_left)
                idx_right = right.index(s[i])
                if idx_left != idx_right:
                    return False

        if len(stack) != 0:
            return False

        return True