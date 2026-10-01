class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            actual_h = 0
            for i in piles:
                actual_h += math.ceil(i / k)
            return actual_h <= h
        
        l, r = 1, max(piles)
        while l < r:
            k = l + (r - l) // 2
            if check(k):
                r = k
            else:
                l = k + 1

        return l