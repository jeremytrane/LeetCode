class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        my_map = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in my_map:
                my_stack.append(c)
            elif my_stack and my_map[my_stack[-1]] == c:
                my_stack.pop()
            else:
                return False

        return not my_stack