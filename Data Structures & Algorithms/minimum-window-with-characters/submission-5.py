class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        T = Counter(t)
        S = dict()
        
        best_length = len(s) + 1
        best_l, best_r = -1, -1

        l = 0
        for r in range(len(s)):
            if s[r] in T:
                S[s[r]] = S.get(s[r], 0) + 1

            while l < r and (s[l] not in T or S.get(s[l], 0) > T.get(s[l], 0)):
                if s[l] in S:
                    S[s[l]] -= 1
                l += 1
            
            flag = True
            for k, v in T.items():
                if S.get(k, 0) < v:
                    flag = False
            
            if flag:
                if r - l + 1 < best_length:
                    best_length = r - l + 1
                    best_l = l
                    best_r = r
        
        if best_l != -1:
            return s[best_l:best_r+1]
        else:
            return ""
