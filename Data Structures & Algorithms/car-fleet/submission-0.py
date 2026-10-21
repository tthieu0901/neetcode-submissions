class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]

        cars.sort(key=lambda x: -x[0])

        stack = []

        for car in cars:
            pos, s = car
            time = (target - pos) / s
            if stack and stack[-1] >= time:
                # car starts after catchup with earlier car
                pass
            else:
                stack.append(time)

        return len(stack)