class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax = nums[0]
        cmin = nums[0]
        answ = nums[0]

        for i in range(1, len(nums)):
            el = nums[i]

            if el < 0:
                cmax, cmin = cmin, cmax
            
            cmax = max(el, cmax * el)
            cmin = min(el, cmin * el)

            answ = max(answ, cmax)

        return answ