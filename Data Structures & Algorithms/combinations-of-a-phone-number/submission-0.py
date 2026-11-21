class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        arr = ['.'] * len(digits)

        def backtrack(idx):
            if idx == len(digits):
                res.append(''.join(arr))
                return

            for char in numToChar[digits[idx]]:
                arr[idx] = char
                backtrack(idx + 1)
        
        if len(digits) == 0:
            return []
            
        backtrack(0)
        return res

