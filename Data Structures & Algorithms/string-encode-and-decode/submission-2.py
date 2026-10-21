class Solution:

    def encodeStr(self, s: str) -> str:
        # Ex. format "\d3\sabc"
        return "/d" + str(len(s)) + "/s" + s

    def decodeStr(self, s: str) -> str:
        # Ex. format "\d3\sabc"
        startLenIdx = 2
        endLenIdx = startLenIdx
        while s[endLenIdx] != '/':
            endLenIdx += 1
        length = int(s[startLenIdx:endLenIdx])

        startContentIdx = endLenIdx + 2
        content = s[startContentIdx:startContentIdx + length]

        return content

    
    def encode(self, strs: List[str]) -> str:
        return ''.join([self.encodeStr(s) for s in strs])

    def decode(self, s: str) -> List[str]:
        i = 0

        decoded = []
        while i < len(s):
            deStr = self.decodeStr(s[i:])
            decoded.append(deStr)
            skip = 4 + len(str(len(deStr))) + len(deStr)
            i += skip

        return decoded