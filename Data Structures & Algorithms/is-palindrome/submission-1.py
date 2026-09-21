class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        l, r = 0, N - 1
        while l < r:
            while l < N and not (s[l].isnumeric() or s[l].isalpha()):
                l += 1 
            while r > 0 and not (s[r].isnumeric() or s[r].isalpha()):
                r -= 1
            
            if l > r:
                return True

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True