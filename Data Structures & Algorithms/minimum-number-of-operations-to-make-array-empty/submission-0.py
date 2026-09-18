class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        answer = 0
        for v in c.values():
            if v == 1:
                return -1
            
            answer += math.ceil(v / 3)
        return answer
                
