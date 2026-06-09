class TimeMap:

    def __init__(self):
        self.stack = defaultdict(list) # key:[value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stack[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.stack:
            return ""

        l, r = 0, len(self.stack[key])-1

        ts = list(self.stack[key])
        while l <= r:
            m = (l+r)//2

            if ts[m][1] == timestamp:
                return ts[m][0]

            if ts[m][1] > timestamp:
                r = m - 1
            else:
                l = m + 1

        if r >= 0:
            return ts[r][0]

        return ""