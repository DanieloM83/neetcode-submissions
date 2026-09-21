class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = Counter(t)
        S = defaultdict(int)

        required = len(T)
        formed = 0

        best_length = len(s) + 1
        res = ""
        l = 0

        for r in range(len(s)):
            S[s[r]] += 1
            if S[s[r]] == T.get(s[r], 0):
                formed += 1
            if formed < required:
                continue
            
            while S[s[l]] > T.get(s[l], 0):
                S[s[l]] -= 1
                l += 1
            
            if r - l + 1 < best_length:
                best_length = r - l + 1
                res = s[l:r + 1]
        
        return res