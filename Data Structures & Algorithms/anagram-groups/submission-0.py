class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            baseStr = str(sorted(s))

            if baseStr not in d:
                d[baseStr] = len(res)
                res.append([s])
            else:
                res[d[baseStr]].append(s)
        
        return res