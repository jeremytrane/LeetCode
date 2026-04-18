class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap = {'(':')', '{':'}', '[':']'}
        for parenthese in s:
            if parenthese in parenthesesMap:
                stack.append(parenthese)
            if parenthese in parenthesesMap.values():
                if stack and parenthese == parenthesesMap[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False