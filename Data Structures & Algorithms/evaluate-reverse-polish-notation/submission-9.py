class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        tokenList = ['+', '-', '*', '/']

        for c in tokens:
            if c in tokenList:
                a = int(stack.pop())
                b = int(stack.pop())

                if c == '+':
                    stack.append(b+a)
                elif c == '-':
                    stack.append(b-a)
                elif c == '*':
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))
            else:
                stack.append(c)
        return int(stack[0])