class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None: # value, timestamp
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values_timestamps = self.map[key]
        l, r = 0, len(values_timestamps)-1
        res = ""

        while l <= r:
            m = (l+r)//2

            if values_timestamps[m][1] <= timestamp:
                res = values_timestamps[m][0]
                l = m + 1
            else:
                r = m - 1
        return res