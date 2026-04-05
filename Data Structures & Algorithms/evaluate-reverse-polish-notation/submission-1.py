class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        signs = ["+", "*","-", '/']
        for token in tokens:
            if token not in signs:
                res.append(int(token))
            else:
                b = res.pop()
                a = res.pop()

                if token == "+":
                    res.append(a + b)
                elif token == "-":
                    res.append(a - b)
                elif token == "*":
                    res.append(a * b)
                elif token == "/":
                    res.append(int(a / b))

        return res[0]

