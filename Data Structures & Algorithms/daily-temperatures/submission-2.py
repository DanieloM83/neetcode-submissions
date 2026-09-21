class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and stack[-1][1] < temp:
                j, _ = stack.pop()
                answer[j] = i - j
            stack.append([i, temp])
        
        return answer