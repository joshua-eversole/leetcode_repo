class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == '-':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == '/':
                num2, num1 = int(stack.pop()), int(stack.pop())
                stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        
        return stack.pop()
                


        