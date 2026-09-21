class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        answer = 0
        for r in range(len(prices)):
            answer = max(answer, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
        
        return answer