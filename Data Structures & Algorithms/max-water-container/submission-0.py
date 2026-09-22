class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        answer = min(heights[l], heights[r]) * (r - l)
        while l < r - 1:
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
            
            answer = max(answer, min(heights[l], heights[r]) * (r - l))
        
        return answer

