class MinStack:

    def __init__(self):
        self.my_stack = [[], []] # Regular stack, min stack

    def push(self, val: int) -> None:
        self.my_stack[0].append(val)
        if self.my_stack[1] and self.my_stack[1][-1] < val:
            self.my_stack[1].append(self.my_stack[1][-1])
        else:
            self.my_stack[1].append(val)

    def pop(self) -> None:
        self.my_stack[0].pop()
        self.my_stack[1].pop()

    def top(self) -> int:
        return self.my_stack[0][-1]

    def getMin(self) -> int:
        return self.my_stack[1][-1]
