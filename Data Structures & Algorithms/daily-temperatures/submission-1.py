class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # стек пустой - значит нету меньше, добавляем себя и ставим 0
        # стек есть - сравниваем себя с верхним. Если верхний больше - добавляем себя и ставим 1
        # стек есть - сравниваем себя с верхним. Если меньше - удаляем, добавляем себе столько, сколько было у него было и идем дальше.
        answer = [0 for i in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):
            curr = 1
            while True:
                if len(stack) == 0:
                    stack.append((temperatures[i], 0))
                    break
                elif stack[-1][0] > temperatures[i]:
                    stack.append((temperatures[i], curr))
                    answer[i] = curr
                    break
                else:
                    _, b = stack.pop()
                    curr += b
            # print(stack)
        
        return answer