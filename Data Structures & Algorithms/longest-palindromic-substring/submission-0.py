class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        n = len(s)

        max_len = 0
        for i in range(n):
            l, r = i, i 
            while l >= 0 and r < n and s[l] == s[r]:
                if len(s[l:r+1]) > max_len:
                    res_idx = l
                    res_len = max_len = r - l + 1
                l -= 1 
                r += 1                         
            
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if len(s[l:r+1]) > max_len:
                    res_idx = l
                    res_len = max_len =  r - l + 1  
                l -= 1
                r += 1
            




        return s[res_idx : res_idx + res_len]



