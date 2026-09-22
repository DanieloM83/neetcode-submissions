class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        pref = [height[0] for i in range(N)]
        suff = [height[-1] for i in range(N)]

        for i in range(1, N):
            pref[i] = max(pref[i-1], height[i])

        for i in range(N-2, -1, -1):
            suff[i] = max(suff[i+1], height[i])
        
        answer = 0
        for i, el in enumerate(height):
            minor = min(pref[i], suff[i])
            answer += minor - el
        
        return answer