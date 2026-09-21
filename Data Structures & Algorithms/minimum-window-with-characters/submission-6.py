class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        T = Counter(t)
        required = len(T)
        
        l = 0
        formed = 0  # how many unique chars
        S = dict()

        best_length = float("inf")
        best_l, best_r = -1, -1

        for r in range(len(s)):
            char = s[r]
            S[char] = S.get(char, 0) + 1

            if char in T and S[char] == T[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < best_length:
                    best_length = r - l + 1
                    best_l = l
                    best_r = r
                left_char = s[l]
                S[left_char] -= 1
                
                if left_char in T and S[left_char] < T[left_char]:
                    formed -= 1
                
                l += 1
        
        if best_length != float('inf'):
            return s[best_l:best_r+1]
        else:
            return ""
