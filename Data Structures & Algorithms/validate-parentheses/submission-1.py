class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque([])
        for i in s:
            if i in ["(", "[", "{"]:
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == ")":
                if stack.pop() != "(":
                    return False
            elif i == "]":
                if stack.pop() != "[":
                    return False
            elif i == "}":
                if stack.pop() != "{":
                    return False
        
        return len(stack) == 0