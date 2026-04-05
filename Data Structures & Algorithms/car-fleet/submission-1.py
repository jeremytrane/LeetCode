class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped_list = sorted(zip(position, speed), reverse=True)
        res = []
        for pos, spe in zipped_list:
            time = (target - pos)/spe
            if res and time > res[-1]:
                res.append(time)
            elif res and time <= res[-1]:
                continue
            else:
                res.append(time)
                
        return len(res)
