class TimeMap:

    def __init__(self):
        self.key_store = defaultdict(list)
        # key -> [(val, timestamp)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append((value, timestamp))
        # guaranteed to be ordered by timestamp

    def get(self, key: str, timestamp: int) -> str:
        res, all = "", self.key_store[key]
        l = 0
        r = len(all) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if all[mid][1] <= timestamp:
                res = all[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

