class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
                newStr += c.lower()
        return newStr == newStr[::-1]