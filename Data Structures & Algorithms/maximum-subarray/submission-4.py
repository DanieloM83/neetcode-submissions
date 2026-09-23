class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        summa = nums[0]

        for r in range(1, len(nums)):
            summa = max(nums[r], summa + nums[r])
            answer = max(answer, summa)
        
        return answer