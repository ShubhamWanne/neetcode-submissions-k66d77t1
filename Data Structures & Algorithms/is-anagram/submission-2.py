class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = set()
        hashT = set()
        if len(s) != len(t):
            return False
        for x,y in zip(sorted(s), sorted(t)):
            if x != y:
                return False
        return True
            