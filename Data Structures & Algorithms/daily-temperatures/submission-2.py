class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i, temperature in enumerate(temperatures):
            
            while stack and temperature > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = i-idx

            stack.append([i, temperature])
        return res