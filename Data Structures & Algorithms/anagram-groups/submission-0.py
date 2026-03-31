class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        result=[]
        for i in range(len(strs)):
            print(f"processing {strs[i]}")
            sorted_str = "".join(sorted(strs[i]))
            print(f"sorted str: {sorted_str}")
            if sorted_str in res:
                print(f"if res: {res}")
                res[sorted_str].append(i)
            else:
                res[sorted_str] = [i]
                print(f"else res: {res}")
        for v in res.values():
            res_t = []
            for i in v:
                res_t.append(strs[i])
            result.append(res_t)
        return result
                