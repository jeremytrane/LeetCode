class Solution:
    def isValid(self, s: str) -> bool:
        bracket_type = {'(':')', '{':'}', '[':']'}
        stack = []

        for bracket in s:
            
            if bracket in bracket_type:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if bracket_type[stack[-1]] != bracket:
                    return False
                stack.pop()                    
        return not stack
            