class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        zipped_list = sorted(zip(position, speed), reverse=True)
        for pos, spe in zipped_list:
            time = (target - pos)/spe
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)