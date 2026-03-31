class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_e = "".join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(s_e)-1
        while(l < r):
            if s_e[l] != s_e[r]: return False
            l += 1
            r -= 1
        return True
        

        