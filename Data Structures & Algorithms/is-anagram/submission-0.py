class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 26 
        if len(s) != len(t):
            return False

        a = [0 for i in range(26)]
        b = [0 for i in range(26)]

        for i in range(len(s)):
            a[ord(s[i]) - ord('a')] += 1
            b[ord(t[i]) - ord('a')] += 1
        
        answer = True
        for i in range(26):
            answer = answer and a[i] == b[i]
        
        return answer