class Solution:
    def check(self, nums: List[int]) -> bool:
        rotations = 0
        N = len(nums)

        for i in range(N):
            if nums[i] > nums[(i + 1) % N]:
                rotations += 1
        
        return rotations <= 1