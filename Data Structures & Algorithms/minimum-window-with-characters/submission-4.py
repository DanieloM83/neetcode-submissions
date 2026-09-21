class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        T = Counter(t)
        S = dict()
        for r in range(len(s)):
            ch = s[r]
            if ch in T:
                S[ch] = S.get(ch, 0) + 1
                flag = True
                for k, v in T.items():
                    if S.get(k, 0) < v:
                        flag = False
                if flag:
                    break

        for k, v in T.items():
            if S.get(k, 0) < v:
                return ""

        best_length = r + 1
        best_l = 0
        best_r = r


        l = 0
        print(l, r)
        while r < len(s) - 1:
            while (s[l] not in T or S[s[l]] > T[s[l]]) and l < r:
                if s[l] in T:
                    S[s[l]] -= 1
                l += 1
            
            length = r - l + 1
            if length < best_length:
                best_length = length
                best_r = r
                best_l = l
            r += 1
            if s[r] in T:
                S[s[r]] += 1
        
        while (s[l] not in T or S[s[l]] > T[s[l]]) and l < r:
                if s[l] in T:
                    S[s[l]] -= 1
                l += 1

        length = r - l + 1
        if length < best_length:
            best_length = length
            best_r = r
            best_l = l

        return s[best_l:best_r+1]
