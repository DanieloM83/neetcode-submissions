class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        for i in tokens:
            if i in "+-/*":
                b = int(stack.pop())
                a = int(stack.pop())
            else:
                a = int(i)

            if i == "+":
                a += b
            elif i == "-":
                a -= b
            elif i == "*":
                a *= b
            elif i == "/":
                a /= b

            stack.append(a)
        return int(stack.pop())
                