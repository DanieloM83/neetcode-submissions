class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i, el1 in enumerate(nums):
            el2 = target - el1
            if el2 in seen:
                return [seen[el2], i]
                
            seen[el1] = i