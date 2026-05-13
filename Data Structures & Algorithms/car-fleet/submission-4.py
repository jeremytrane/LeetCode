class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        zippedList = sorted(zip(position, speed), reverse=True)

        for pos, spe in zippedList:
            distance = target - pos
            time = (distance/spe)
            if not stack:
                stack.append(time)
                
            if stack and time > stack[-1]:
                stack.append(time)
        return len(stack)