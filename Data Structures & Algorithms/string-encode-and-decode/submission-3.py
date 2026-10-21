class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "|" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        cur = 0
        res = []
        while cur < len(s):
            l = ""
            while cur < len(s) and s[cur] != '|':
                l += s[cur]
                cur += 1
            
            decoded_size = int(l)

            decoded = ""
            cur += 1
            for i in range(decoded_size):
                decoded += s[cur]
                cur += 1

            res.append(decoded)


        return res