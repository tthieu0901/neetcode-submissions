class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []

        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while s and t > temperatures[s[-1]]:
                top = s.pop()
                res[top] = i - top

            s.append(i)
        
        return res