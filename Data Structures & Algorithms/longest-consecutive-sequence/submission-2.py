class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        items = Counter(nums)

        answer = 0
        for i in set(nums):
            if items.get(i - 1) is None:
                j = i
                local = 1
                while items.get(j + 1):
                    j = j + 1
                    local += 1
                answer = max(answer, local)
        
        return answer
        