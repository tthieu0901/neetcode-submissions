class MinStack:

    def __init__(self):
        self.data = []
        self.minValue = []

    def push(self, value: int) -> None:
        self.data.append(value)
        if self.minValue:
            self.minValue.append(min(self.minValue[-1], value))
        else:
            self.minValue.append(value)

    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.minValue.pop()

    def top(self) -> int:
        return self.data[-1] if self.data else None

    def getMin(self) -> int:
        return self.minValue[-1]
        