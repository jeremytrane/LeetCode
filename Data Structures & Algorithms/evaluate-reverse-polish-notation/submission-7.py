class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operands = ['+', '-', '*', '/']
        stack = []

        for ch in tokens:
            if ch in operands:
                a = int(stack.pop())
                b = int(stack.pop())
                if ch == '+':
                    stack.append(b+a)
                elif ch == '-':
                    stack.append(b-a)
                elif ch == '*':
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(ch)
        return int(stack[0])