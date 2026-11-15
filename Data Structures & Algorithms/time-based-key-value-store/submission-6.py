class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals:
            self.vals[key] = [(timestamp, value)]
        else:
            self.vals[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""

        arr = self.vals[key]
        def max_smaller_than_target(target):
            left, right = 0, len(arr)

            while left < right:
                mid = left + (right - left) // 2
                t = arr[mid][0]
                if t <= target:
                    left = mid + 1
                else:
                    right = mid

            return left - 1

        idx = max_smaller_than_target(timestamp)
        return "" if idx == -1 else arr[idx][1]
