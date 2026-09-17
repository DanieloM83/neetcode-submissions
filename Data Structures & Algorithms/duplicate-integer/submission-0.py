class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = dict()
        answer = False
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            answer = answer or (counter[i] > 1)
        
        return answer