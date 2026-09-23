class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        summa = nums[0]

        l = 0
        for r in range(1, len(nums)):
            summa += nums[r]
            while summa < nums[r] and l < r:
                summa -= nums[l]
                l += 1
            # print(l, r, "-", summa)
            answer = max(answer, summa)
        
        return answer